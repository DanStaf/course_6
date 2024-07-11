import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from apscheduler.schedulers.background import BackgroundScheduler

from mailing.models import Client, MailingSettings, MailingAttempt


# from config.settings import CACHE_ENABLED


def set_owner(self, form, object_is_new=True):

    self.object = form.save()

    if object_is_new:
        self.object.owner = self.request.user
        self.object.save()


def check_user_is_owner_or_su(self, model_):
    pk = self.kwargs.get('pk')
    object_ = get_object_or_404(model_, pk=pk)
    return (self.request.user == object_.owner) or self.request.user.is_superuser


def send_mailing():

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # now: 13:43, got: 2024-07-11 10:43:31.192337+00:00

    mailings = MailingSettings.objects.filter(first_sent_datetime__lte=current_datetime).filter(
        status__in=[MailingSettings.STARTED, MailingSettings.CREATED])

    qty_success = 0
    qty_fail = 0
    qty_passed = 0
    qty_inactive = len(MailingSettings.objects.all())-len(mailings)

    for mailing in mailings:
        attempts = MailingAttempt.objects.filter(mailing=mailing)
        if attempts:
            a_list = [item.sent_datetime for item in attempts]
            last_attempt_datetime = max(a_list)

            if mailing.period == MailingSettings.DAILY:
                td = timedelta(days=1)
            elif mailing.period == MailingSettings.WEEKLY:
                td = timedelta(weeks=1)
            elif mailing.period == MailingSettings.MONTHLY:
                td = timedelta(days=30)
            else:
                td = timedelta(days=0)
            next_attempt_datetime = last_attempt_datetime + td
        else:
            next_attempt_datetime = mailing.first_sent_datetime

        # next try: 2024-07-11 01:21:00+00:00
        # now:      2024-07-11 10:43:31.192337+00:00
        # print(f'{mailing.mailing_text.topic}: next try: {next_attempt_datetime} / now: {current_datetime} / {next_attempt_datetime <= current_datetime}')

        if next_attempt_datetime <= current_datetime:
            mailing.status = MailingSettings.STARTED
            mailing.save()

            try:
                server_response = send_mail(
                    subject=mailing.mailing_text.topic,
                    message=mailing.mailing_text.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.clients.all()],
                    fail_silently=False,
                )
                new_attempt = MailingAttempt.objects.create(status=MailingAttempt.SUCCESS,
                                              server_reply=server_response,
                                              mailing=mailing, )
                qty_success += 1

            except smtplib.SMTPException as e:
                new_attempt = MailingAttempt.objects.create(status=MailingAttempt.FAIL,
                                              server_reply=str(e),
                                              mailing=mailing, )
                qty_fail += 1

        else:
            qty_passed += 1

    qty_active = qty_success + qty_fail + qty_passed
    qty_total = qty_active + qty_inactive

    print(f'success: {qty_success}, fail: {qty_fail}, passed: {qty_passed} / total active: {qty_active}')
    print(f'finished or not started: {qty_inactive} / total: {qty_total}')


def start_scheduler():
    scheduler = BackgroundScheduler()

    if not scheduler.get_jobs():
        scheduler.add_job(send_mailing, 'interval', seconds=10)

    if not scheduler.running:
        scheduler.start()
