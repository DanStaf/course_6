import random
import string
import secrets

from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from users.forms import RegisterForm, ProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse

from config.settings import EMAIL_HOST_USER


def main_view(request):
    context = {"object": 'users'}
    return render(request, 'main/test.html', context=context)


class RegisterView(CreateView):

    model = User
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}'

        send_mail(
            "Skystore - email confirm",
            f"To confirm the email please tap on the link: {url}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    return redirect(reverse("users:login"))


class UserProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserResetPasswordView(PasswordResetView):
    model = User
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'

    def form_valid(self, form):

        form_email = form.cleaned_data.get("email")
        user = User.objects.get(email=form_email)

        ### new pass

        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(10))
        # password = User.objects.make_random_password(10)  # ?????

        user.set_password(new_password)
        user.save()

        ### send email

        send_mail(
            "Skystore - new password generated",
            f"Please use the below password: {new_password}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        return redirect(reverse("users:login"))


class UserResetPasswordDoneView(PasswordResetView):
    model = User
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:login')
