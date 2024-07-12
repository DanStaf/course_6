from django.db import models

from users.models import User


class Client(models.Model):
    email = models.EmailField(verbose_name='Почта', unique=True)
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий')
    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Владелец', on_delete=models.SET_NULL)

    def __str__(self):
        # Строковое отображение объекта
        return f'CLIENT: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class MailingText(models.Model):
    topic = models.TextField(verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Владелец', on_delete=models.SET_NULL)

    def __str__(self):
        # Строковое отображение объекта
        max_len = 10 if len(self.topic) > 10 else len(self.topic)
        return f'MailingText: {self.topic[:max_len]}...'
        # return f'MailingText: {self.topic}'

    class Meta:
        verbose_name = 'рассылка (текст)'
        verbose_name_plural = 'рассылки (текст)'


class MailingSettings(models.Model):

    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    first_sent_datetime = models.DateTimeField(verbose_name='дата и время первой отправки')
    period = models.CharField(
        max_length=150,
        choices=PERIODICITY_CHOICES,
        default=DAILY,
        verbose_name="Периодичность",
    )
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус")

    # one (text) to many (settings)
    mailing_text = models.ForeignKey(MailingText, null=True, verbose_name='Текст рассылки', on_delete=models.SET_NULL)

    # many (clients) to many (settings)
    clients = models.ManyToManyField(Client)

    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Владелец', on_delete=models.SET_NULL)

    def __str__(self):
        # Строковое отображение объекта
        return f'MailingSettings: {self.mailing_text}'

    class Meta:
        verbose_name = 'рассылка (настройки)'
        verbose_name_plural = 'рассылки (настройки)'
        permissions = [
            ('deactivate_mailing', 'Can deactivate mailing'),
            ('view_all_mailings', 'Can view all mailings'),
        ]


class MailingAttempt(models.Model):
    SUCCESS = 'Успешно'
    FAIL = 'Неуспешно'
    STATUS_VARIANTS = [
        (SUCCESS, 'Успешно'),
        (FAIL, 'Неуспешно'),
    ]

    sent_datetime = models.DateTimeField(verbose_name='дата и время попытки', auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_VARIANTS, verbose_name='Cтатус рассылки')
    server_reply = models.TextField(verbose_name='ответ почтового сервера', null=True, blank=True)

    # one (setting) to many (attempts)
    mailing = models.ForeignKey(MailingSettings, verbose_name='Настройка рассылки', on_delete=models.CASCADE)

    def __str__(self):
        # Строковое отображение объекта
        return f'MailingAttempt: {self.mailing}'

    class Meta:
        verbose_name = 'рассылка (попытка)'
        verbose_name_plural = 'рассылки (попытки)'
