from django.core.cache import cache
from django.shortcuts import get_object_or_404
from apscheduler.schedulers.background import BackgroundScheduler

from mailing.models import Client
# from config.settings import CACHE_ENABLED


def set_owner(self, form, object_is_new=True, status=None, status_model=None):

    self.object = form.save()

    if object_is_new:
        self.object.owner = self.request.user
        if status is not None:
            self.object.status = status_model.objects.get(name=status)

        self.object.save()


def check_user_is_owner_or_su(self, model_):
    pk = self.kwargs.get('pk')
    object_ = get_object_or_404(model_, pk=pk)
    return (self.request.user == object_.owner) or self.request.user.is_superuser


def send_mailing():
    print('__Send mailing__')


def start_scheduler():
    scheduler = BackgroundScheduler()

    # ????????, ????????? ?? ?????? ???
    if not scheduler.get_jobs():
        scheduler.add_job(send_mailing, 'interval', seconds=10)

    if not scheduler.running:
        scheduler.start()
