from django.urls import path
from main.apps import MainConfig
from main.views import main_view

app_name = MainConfig.name

urlpatterns = [
    path('', main_view, name='home'),
]
