from django.contrib import admin

from mailing.models import Client, StatusAttempt, StatusMailing, Period, MailingText, MailingSettings, MailingAttempt


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment')


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'days')


@admin.register(StatusMailing)
class StatusMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(StatusAttempt)
class StatusAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(MailingText)
admin.site.register(MailingSettings)
admin.site.register(MailingAttempt)
