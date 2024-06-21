from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import main_view

app_name = MailingConfig.name

urlpatterns = [
    path('', main_view, name='home'),
]