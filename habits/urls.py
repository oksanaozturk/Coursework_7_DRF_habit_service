from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitRetrieveAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name


urlpatterns = [
    # Путь для вывода страницы со всеми объектами модели Habit
    path("habits/", HabitListAPIView.as_view(), name="habits-list"),
    # Путь для вывода страницы с одним объектом модели Habit
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits-retrieve"),
    # Путь для вывода страницы при создании нового объекта модели Habit
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits-create"),
    # Путь для редактирования объекта модели Habit
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits-update"),
    # Путь для удаления объекта модели Habit
    path("habits/<int:pk>/destroy/", HabitDestroyAPIView.as_view(), name="habits-destroy"),

    # Путь для вывода Всех Публичных привычек
    path('public/', PublicHabitListAPIView.as_view(), name='public'),
]
