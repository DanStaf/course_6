from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MailingTextForm
from mailing.models import Client, MailingText
from mailing.services import set_owner, check_user_is_owner_or_su

# Create your views here.


def main_view(request):
    context = {"object": 'mailing'}
    return render(request, 'mailing/mailing.html', context=context)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    login_url = "/users/login/"


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    login_url = "/users/login/"


class ClientCreateUpdate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form, object_is_new=True):
        if form.is_valid():
            set_owner(self, form, object_is_new)
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ClientCreateView(LoginRequiredMixin, ClientCreateUpdate, CreateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, True)


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, ClientCreateUpdate, UpdateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, False)

    def test_func(self):
        return check_user_is_owner_or_su(self, Client)


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    login_url = "/users/login/"

    def test_func(self):
        return check_user_is_owner_or_su(self, Client)


###


class MailingTextListView(LoginRequiredMixin, ListView):
    model = MailingText
    login_url = "/users/login/"


class MailingTextDetailView(LoginRequiredMixin, DetailView):
    model = MailingText
    login_url = "/users/login/"


class MailingTextCreateUpdate(CreateView):
    model = MailingText
    form_class = MailingTextForm
    success_url = reverse_lazy('mailing:text_list')

    def form_valid(self, form, object_is_new=True):
        if form.is_valid():
            set_owner(self, form, object_is_new)
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class MailingTextCreateView(LoginRequiredMixin, MailingTextCreateUpdate, CreateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, True)


class MailingTextUpdateView(LoginRequiredMixin, UserPassesTestMixin, MailingTextCreateUpdate, UpdateView):
    login_url = "/users/login/"

    def form_valid(self, form, *args):
        return super().form_valid(form, False)

    def test_func(self):
        return check_user_is_owner_or_su(self, MailingText)


class MailingTextDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailingText
    success_url = reverse_lazy('mailing:text_list')
    login_url = "/users/login/"

    def test_func(self):
        return check_user_is_owner_or_su(self, MailingText)
