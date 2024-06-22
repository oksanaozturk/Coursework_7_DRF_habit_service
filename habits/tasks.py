from celery import shared_task
from django.utils import timezone

from config import settings
from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_tg_habits_message():
    """
    Функуия ТГ-рассылки напоминаний о том, в какое время и какие
    привычки необходимо выполнять, если дата выполнения - сегодня.
    :return:
    """

    today = timezone.now().time()  # .today().date отобразится в формате времени
    print(today)
    habits = Habit.objects.all()  # фильтруем привычки

    for habit in habits:
        if habit.time <= today:
            # Формируем сообщение для текущей привычки
            message = f"Привет! Тебя ждет полезная привычка {habit.action} в {habit.time}, место - {habit.place}"
            send_tg_message(settings.TELEGRAM_CHAT_ID, message)

        # Обновление времени выполнения привычки в зависимости от periodicity
        # if habit.periodicity == 1:
        #     habit.time += today.timedelta(days=1)
        # elif habit.periodicity == 2:
        #     habit.time += today.timedelta(days=2)
        # elif habit.periodicity == 3:
        #     habit.time += today.timedelta(days=3)
        # elif habit.periodicity == 4:
        #     habit.time += today.timedelta(days=4)
        # elif habit.periodicity == 5:
        #     habit.time += today.timedelta(days=5)
        # elif habit.periodicity == 6:
        #     habit.time += today.timedelta(days=6)
        # elif habit.periodicity == 7:
        #     habit.time += today.timedelta(days=7)
        # habit.save()
