from django.db import models

from users.models import User


class Period(models.Model):
    """'раз в день', 1"""

    name = models.CharField(verbose_name='Название')
    days = models.PositiveIntegerField(verbose_name='Периодичность в днях')

    def __str__(self):
        # Строковое отображение объекта
        return f'PERIOD: {self.name}'

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'периоды'


class StatusMailing(models.Model):
    """'завершена', 'создана', 'запущена'"""

    name = models.CharField(verbose_name='Название')

    def __str__(self):
        # Строковое отображение объекта
        return f'STATUS: {self.name}'

    class Meta:
        verbose_name = 'статус рассылки'
        verbose_name_plural = 'статусы рассылок'


class StatusAttempt(models.Model):
    """'успешно', 'не успешно'"""

    name = models.CharField(verbose_name='Название')

    def __str__(self):
        # Строковое отображение объекта
        return f'STATUS: {self.name}'

    class Meta:
        verbose_name = 'статус попытки'
        verbose_name_plural = 'статусы попыток'


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
    first_sent_datetime = models.DateTimeField(verbose_name='дата и время первой отправки')
    period = models.CharField(max_length=150, verbose_name='периодичность')
    status = models.ForeignKey(StatusMailing, null=True, verbose_name='Статус', on_delete=models.SET_NULL)

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


class MailingAttempt(models.Model):
    sent_datetime = models.DateTimeField(verbose_name='дата и время попытки')
    status = models.ForeignKey(StatusAttempt, null=True, verbose_name='Статус', on_delete=models.SET_NULL)
    server_reply = models.TextField(verbose_name='ответ почтового сервера')

    # one (setting) to many (attempts)
    mailing = models.ForeignKey(MailingSettings, verbose_name='Настройка рассылки', on_delete=models.CASCADE)

    def __str__(self):
        # Строковое отображение объекта
        return f'MailingAttempt: {self.mailing}'

    class Meta:
        verbose_name = 'рассылка (попытка)'
        verbose_name_plural = 'рассылки (попытки)'
