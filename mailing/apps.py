from time import sleep

from config.settings import RUN_MAILING_SCHEDULE
from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        if RUN_MAILING_SCHEDULE == 'TRUE':
            from mailing.services import start_scheduler
            sleep(2)
            start_scheduler()
            print('scheduler started')
        else:
            print('scheduler not started')
