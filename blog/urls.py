from django.urls import path
from blog.apps import BlogConfig
from blog.views import main_view

app_name = BlogConfig.name

urlpatterns = [
    path('', main_view, name='home'),
]