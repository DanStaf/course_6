from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import main_view, ClientListView, ClientCreateView, ClientDetailView, ClientDeleteView, \
    ClientUpdateView, MailingTextListView, MailingTextCreateView, MailingTextDetailView, MailingTextUpdateView, \
    MailingTextDeleteView, MailingSettingsCreateView, MailingSettingsListView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView, MailingAttemptListView, change_status

app_name = MailingConfig.name

urlpatterns = [
    path('', main_view, name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('clients/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('text/', MailingTextListView.as_view(), name='text_list'),
    path('text/create', MailingTextCreateView.as_view(), name='text_create'),
    path('text/<int:pk>', MailingTextDetailView.as_view(), name='text_detail'),
    path('text/update/<int:pk>', MailingTextUpdateView.as_view(), name='text_update'),
    path('text/delete/<int:pk>', MailingTextDeleteView.as_view(), name='text_delete'),

    path('settings/', MailingSettingsListView.as_view(), name='settings_list'),
    path('settings/create', MailingSettingsCreateView.as_view(), name='settings_create'),
    path('settings/<int:pk>', MailingSettingsDetailView.as_view(), name='settings_detail'),
    path('settings/update/<int:pk>', MailingSettingsUpdateView.as_view(), name='settings_update'),
    path('settings/delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='settings_delete'),
    path('settings/change_status/<int:pk>', change_status, name='settings_change_status'),

    path('log/', MailingAttemptListView.as_view(), name='log_list'),
]
