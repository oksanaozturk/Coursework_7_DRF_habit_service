from datetime import datetime, timedelta
import requests

from celery import shared_task

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
    time_now = datetime.now().time().replace(second=0, microsecond=0)
    date_now = datetime.now().date()
    print(time_now, date_now)
    # фильтруем привычки, те у которых есть хозяин и не являются связанными(т.е.приятными привычками в качестве награлы)
    habits = Habit.objects.filter(owner__is_active=True, is_pleasant_habit=False)

    for habit in habits:
        if habit.send_date == date_now:
            # Формируем сообщение для текущей привычки
            message = f"Привет! Сегодня Тебя ждет полезная привычка {habit.action} в {habit.time}, место -{habit.place}"
            try:
                send_tg_message(settings.TELEGRAM_CHAT_ID, message)
                get_date_send(habit, date_now)

            except requests.RequestException as e:
                print(f"Ошибка при отправке сообщения в Telegram: {e}")

            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")


def get_date_send(habit, date_now):
    """
    Функция Обновление времени выполнения привычки в зависимости от periodicity (send_next_date).
    """
    if habit.send_date <= date_now:
        if habit.periodicity == 1:
            habit.send_date += timedelta(days=1)
        elif habit.periodicity == 2:
            habit.send_date += timedelta(days=2)
        elif habit.periodicity == 3:
            habit.send_date += timedelta(days=3)
        elif habit.periodicity == 4:
            habit.send_date += timedelta(days=4)
        elif habit.periodicity == 5:
            habit.send_date += timedelta(days=5)
        elif habit.periodicity == 6:
            habit.send_date += timedelta(days=6)
        elif habit.periodicity == 7:
            habit.send_date += timedelta(days=7)
        habit.save()
