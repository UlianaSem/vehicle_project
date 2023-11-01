# vehicle project

## Описание проекта

Проект приложения для продажи транспортных средств.

В рамках проекта реализована бэкенд-часть SPA веб-приложения. 

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Redis
- Celery

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Документация

Документация находится по ссылкам:
1. Swagger `swagger/`
2. Redoc `redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Redis на компьютер командой `sudo apt install redis`
2. Cклонируйте репозиторий себе на компьютер
3. Установите необходимые зависимости командой `poetry install`
4. Создайте БД
5. Создайте файл .env и заполните его, используя образец из файла .env.example
6. Выполните миграции командой `python manage.py migrate`
7. Запустите Celery worker командой `celery -A config worker --loglevel=info`
8. Как отдельный процесс запустите Celery beat командой `celery -A config beat --loglevel=info`

## Файл .env.example

1. `DATABASES_NAME, DATABASES_USER, DATABASES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_SSL` - данные для осуществления Email рассылки
3. `EXCHANGE_RATE_API_KEY`, `EXCHANGE_RATE_URL` - данные для подключения к apilayer
4. `SECRET_KEY, DEBUG`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
