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
            email="test@test.ru",
            password="test",
        )
        # принудительная аутентификация клиента с помощь метода force_authenticate
        # (так как только авторизованные Пользователи могут работать в системе)
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place="В любом месте",
            time="10:00:00",
            action="Выполнить 20 приседаний",
            is_pleasant_habit=False,
            periodicity=1,
            bonus="Получишь 100 рублей",
            execution_duration=90,
            is_public=True,
        )

    def test_habit_create(self):
        """
        Тест для проверки работы create(POST) - Создание новой привычки.
        """

        # Получаем url для create.
        url = reverse("habits:habits-create")
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
            "is_public": True,
        }
        # После находжения url делаем запрос (POST), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.post(url, data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_delete(self):
        """
        Тест для проверки работы delete/destroy(DELETE) - удаление урока по указанию pk(id) привычки в запросе.
        """
        # Получаем url.
        url = reverse("habits:habits-destroy", args=(self.habit.pk,))
        # После находжения url делаем запрос (DELETE), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.delete(url)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            Habit.objects.all().count(),
            0,  # Так как из базы данных был удален объект 1 (создано 1)
        )

    def test_habit_retrieve(self):
        """
        Тест для проверки работы retrieve(GET) - получение данных привычки по указанию pk(id) в запросе.
        """
        # Получаем url
        url = reverse("habits:habits-retrieve", args=(self.habit.pk,))
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        # Полученные в response данные преобразуем в json
        data = response.json()
        # print(data)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data.get("bonus"),
            self.habit.bonus,  # Второе значение можно написать как "Получишь 100 рублей"
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": "В любом месте",
                "time": "10:00:00",
                "action": "Выполнить 20 приседаний",
                "is_pleasant_habit": False,
                "periodicity": 1,
                "bonus": "Получишь 100 рублей",
                "execution_duration": 90,
                "is_public": True,
                "start_date": self.habit.start_date.strftime("%Y-%m-%d"),
                "send_date": self.habit.send_date.strftime("%Y-%m-%d"),
                "owner": self.user.pk,
                "associated_habit": None,
            },
        )

    def test_habit_update(self):
        """
        Тест для проверки работы update(PUT/PATCH) -
        внесение изменений в данные урока по указанию pk(id) привычки в запросе.
        """
        # Получаем url
        url = reverse("habits:habits-update", args=(self.habit.pk,))
        # Задаем данные для внесение изменений в данные урока:
        data = {
            "bonus": "Test_bonus",
        }
        # После находжения url делаем запрос (PATCH), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.patch(url, data)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data.get("bonus"),
            "Test_bonus",  # Так как были внесены изменения "Тест урока" поменялся на "Test"
        )

    def test_habit_list(self):
        """
        Тест на проверку работы настройки Пагинации (выведение заданного количества сущностей на страницу).
        """
        # Получаем url для вывода всех курсов
        url = reverse("habits:habits-list")
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        data = response.json()
        # print(data)  # Выводим, чтобы визуально сравнить данные
        # Берем пример данных, которые у нас будут выдаваться из Postman, меняя на значения, которые у нас будут
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "В любом месте",
                    "time": "10:00:00",
                    "action": "Выполнить 20 приседаний",
                    "is_pleasant_habit": False,
                    "periodicity": 1,
                    "bonus": "Получишь 100 рублей",
                    "execution_duration": 90,
                    "is_public": True,
                    "send_date": self.habit.send_date.strftime("%Y-%m-%d"),
                    "start_date": self.habit.start_date.strftime("%Y-%m-%d"),
                    "owner": self.user.pk,
                    "associated_habit": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK),
        self.assertEqual(data, result)  # Сравниваем эти 2 значения

    def test_public_habit_list(self):
        """
        Тест на проверку работы настройки Пагинации (выведение заданного количества сущностей на страницу)
        и вывода всех публичных привычек на страницу.
        """
        # Получаем url для вывода всех курсов
        url = reverse("habits:public")
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        # data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_execution_duration_habit(self):
        """
        Тестирование создания привычки со временем исполнения более 2 минут.
        """

        url = reverse("habits:habits-create")
        data = {
            "place": "test_place",
            "time": "13:00:00",
            "action": "test_action",
            "is_pleasant_habit": False,
            "associated_habit": 4,
            "execution_duration": 130,
            "is_public": True,
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_periodicity_habit(self):
        """
        Тестирование создания привычки с periodicity больше 7.
        """

        url = reverse("habits:habits-create")
        data = {
            "place": "test_place9",
            "time": "13:00:00",
            "action": "test_action9",
            "is_pleasant_habit": False,
            "associated_habit": 4,
            "execution_duration": 110,
            "periodicity": 8,
            "is_public": True,
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
