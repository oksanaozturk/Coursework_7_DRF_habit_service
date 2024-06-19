from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """
    Класс для тестирования CRUD модели Habit (контролеры были созданы с помощью дженериков).
    """

    def setUp(self):
        """Метод для предоставления тестового объекта."""
        self.client = APIClient()
        # Создание Пользователя
        self.user = User.objects.create(
            email='test@test.ru',
            password='test',
        )
        # принудительная аутентификация клиента с помощь метода force_authenticate
        # (так как только авторизованные Пользователи могут работать в системе)
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(owner=self.user,
                                          place='В любом месте',
                                          time='10:00:00',
                                          action='Выполнить 20 приседаний',
                                          is_pleasant_habit=False,
                                          periodicity=1,
                                          bonus="Получишь 100 рублей",
                                          execution_duration=90,
                                          is_public=True)

        self.pleasant_habit = Habit.objects.create(owner=self.user,
                                                   place='Ванная комната',
                                                   time='20:00',
                                                   action='Ванна с пеной',
                                                   is_pleasant_habit=True,
                                                   is_public=True)

    def test_habit_create(self):
        """
        Тест для проверки работы create(POST) - Создание новой привычки.
        """

        # Получаем url для create.
        url = reverse('habits:habits-create')
        # Задаем данные для создания курса:
        data = {
                # "owner": self.user,
                "place": "test_place",
                "time": "10:00:00",
                "action": "test_action",
                "is_pleasant_habit": False,
                "periodicity": 1,
                "bonus": "test_bonus",
                "execution_duration": 90,
                "is_public": True
        }
        # После находжения url делаем запрос (POST), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.post(url, data)
        print(response.json)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 3)

    def test_habit_delete(self):
        """
        Тест для проверки работы delete/destroy(DELETE) - удаление урока по указанию pk(id) привычки в запросе.
        """
        # Получаем url.
        url = reverse('habits:habits-destroy', args=(self.habit.pk,))
        # После находжения url делаем запрос (DELETE), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.delete(url)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 1  # Так как из базы данных был удален объект 1 (создано 2)
        )
