from django.urls import path
from main.apps import MainConfig
from mailing.views import main_view

app_name = MainConfig.name

urlpatterns = [
    path('', main_view, name='home'),
]
