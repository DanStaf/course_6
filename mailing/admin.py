from django.contrib import admin
from mailing.models import Client, MailingText, MailingSettings, MailingAttempt

admin.site.register(Client)
admin.site.register(MailingText)
admin.site.register(MailingSettings)
admin.site.register(MailingAttempt)
