from celery import shared_task
from django.utils import timezone


# тестовая задача проверки celery
@shared_task
def send_tg_habits_reminder():
    today = timezone.now().today().date
    print(today)


# @shared_task
# def send_tg_habits_reminder():
#     '''ТГ-рассылка напоминаний о том, в какое время и какие
#     привычки необходимо выполнять, если дата выполнения - сегодня.'''
#
#     today = timezone.now().time()     # .today().date отобразится в формате времени
#     print(today)
#     habits = Habit.objects.all()     # фильтруем привычки
#
#     for habit in habits:
#         # Проверяем, что у пользователя есть telegram_id и время выполнения привычки соответствует сегодняшнему дню
#         if habit.owner.telegram_id:
#             # Формируем сообщение для текущей привычки
#             message = f'Привет! Выполни привычку {habit.action} в {habit.time}, место - {habit.location}'
#             send_tg_message(habit.owner.telegram_id, message)
#
#         # Обновление времени выполнения привычки в зависимости от periodicity
#         if habit.periodicity == 1:
#             habit.time += today.timedelta(days=1)
#         elif habit.periodicity == 2:
#             habit.time += today.timedelta(days=2)
#         elif habit.periodicity == 3:
#             habit.time += today.timedelta(days=3)
#         elif habit.periodicity == 4:
#             habit.time += today.timedelta(days=4)
#         elif habit.periodicity == 5:
#             habit.time += today.timedelta(days=5)
#         elif habit.periodicity == 6:
#             habit.time += today.timedelta(days=6)
#         elif habit.periodicity == 7:
#             habit.time += today.timedelta(days=7)
#         habit.save()
