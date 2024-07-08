from django.core.management import BaseCommand
from mailing.models import Period, StatusMailing, StatusAttempt


class Command(BaseCommand):

    def handle(self, *args, **options):
        period_1 = Period.objects.create(name='Раз в день', days=1)
        period_1.save()

        period_2 = Period.objects.create(name='Раз в неделю', days=7)
        period_2.save()

        period_3 = Period.objects.create(name='Раз в месяц', days=30)
        period_3.save()

        m_status_1 = StatusMailing.objects.create(name='Создана')
        m_status_1.save()

        m_status_2 = StatusMailing.objects.create(name='Запущена')
        m_status_2.save()

        m_status_3 = StatusMailing.objects.create(name='Завершена')
        m_status_3.save()

        a_status_1 = StatusAttempt.objects.create(name='Успешно')
        a_status_1.save()

        a_status_2 = StatusAttempt.objects.create(name='Не успешно')
        a_status_2.save()
