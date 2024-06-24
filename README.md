## Coursework_7_DRF_habit_service

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек 
и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать 
трекер полезных привычек.

В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.

### Используемые технологии:

 - Python
 - Django
 - PostgerSQL
 - Django REST framework
 - celery
 - celery-beat
 - redis

<details>
<summary> Инструкция по развертыванию проекта</summary>


1) ### Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла env.sample

#### Добавьте секретный ключ Вашего проекта
SECRET_KEY=

#### Добавте настройки для подключения к базе данных (ДБ должна быть создана)
 - POSTGRES_DB=
 - POSTGRES_USER=
 - POSTGRES_HOST=
 - POSTGRES_PORT=
 - POSTGRES_PASSWORD=

#### Настройки для отправки сообщения в Телеграмм-бот
 - BOT_TOKEN=

#### Добавьте настройки для celery
 - CELERY_BROKER_URL=
 - CELERY_RESULT_BACKEND=)


2) ### Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt
  - pip install -r requirements.txt

3) ### Команда для запуска Приложения: 
  - python manage.py runserver

4) ### Команда для запуска redis: 
  - Для Windows в терминале UBUNTU командой redis-server

5) ### Команда для запуска celery-bea и celery worker одной командой:
  - celery -A condig worker --beat --scheduler django --loglevel=info
  - Для Windows (в разных Pycharm запустите команды): 
    * celery -A config worker -l INFO -P eventlet
    * celery -A config beat -l INFO -S django

</details>

### Автор проекта https://github.com/oksanaozturk