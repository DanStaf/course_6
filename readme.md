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
- скрипт рассылки запускается по расписанию (через apps.py).

