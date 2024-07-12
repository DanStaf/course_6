from django.urls import path
from users.apps import UsersConfig

from users.views import main_view
from users.views import (RegisterView, UserProfileView, UserResetPasswordView, email_verification,
                         UserDeleteView, UserListView, user_change_active)
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    # path('', main_view, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
    path('delete/', UserDeleteView.as_view(), name='user_delete'),

    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', UserResetPasswordView.as_view(), name='password_reset'),

    path('', UserListView.as_view(), name='users'),
    path('change_active/<int:pk>/', user_change_active, name='change_active'),
]
