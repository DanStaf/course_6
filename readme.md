# course 6 / Django

## Модели
### Приложение "Сервис рассылок"
- Client
- MailingText
- MailingSettings
- MailingAttempt

### Приложение пользователи
- User

### Приложение блог
- Article

## Главная страница
- количество рассылок всего, 
- количество активных рассылок, 
- количество уникальных клиентов для рассылок, 
- три случайные статьи из блога.

## Пример:
- компания N захотела создать на нашем сервисе рассылку.
- Создала для нее сообщение, которое будет отправлено клиентам,
- наполнила базу клиентов своими данными с помощью графического интерфейса сайта,
- затем перешла к созданию рассылки: указала необходимые параметры, сообщение и выбрала клиентов, которым эта рассылка должна быть отправлена.

## Как использовать:
- скрипт рассылки, который работает из командной строки 'runmailing'.
- скрипт рассылки запускается по расписанию.

# Функция старта периодических задач 
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(функция_отправки_письма, 'interval', seconds=10)
    scheduler.start()

# Главная функция по отправке рассылки
def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Модель_рассылки.objects.filter(дата__lte=current_datetime).filter(
        статус_рассылки__in=[список_статусов])

    for mailing in mailings:
        send_mail(
                subject=theme,
                message=text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.клиенты.all()]
           )

Ответ почтового сервера можно получить из функции 
send_mail()
. Укажите параметр 
fail_silently=False
 и обработайте ошибки группы 
smtplib.SMTPException
.

try:
	# Отправляем письмо
	server_response = send_mail(... , fail_silently=False)
	Попытка рассылки.objects.create(...)
except smtplib.SMTPException as e:
	# При ошибке почтовика получаем ответ сервера - ошибка, которая записывается в е
	Попытка рассылки.objects.create(...)

# анализ попыток рассылок
Попытка_рассылки.objects.filter(рассылка=рассылка).order_by('-дата_рассылки').first()

...
if рассылка.периодичность == Ежедневная_приодичность and разница_времени_текущего_и_последней_отправки.days >= 1:
   next_send_time = дата_последней_отправки + timezone.timedelta(days=1, hours=рассылка.time.hour,
                                                                        minutes=рассылки.time.minute)
...
