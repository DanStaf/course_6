from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import main_view, ClientListView, ClientCreateView, ClientDetailView, ClientDeleteView, \
    ClientUpdateView

app_name = MailingConfig.name

urlpatterns = [
    path('', main_view, name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('clients/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

]
