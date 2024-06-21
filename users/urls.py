from django.urls import path
from users.apps import UsersConfig
from users.views import main_view

app_name = UsersConfig.name

urlpatterns = [
    path('', main_view, name='home'),
]