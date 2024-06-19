from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    """Класс для создания экземпляра модели Habit (CRUD)"""
    serializer_class = HabitSerializer

    # Необходимо указать IsAuthenticated, так как вносятся изменения на уровне проекта
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Метод для присоединения создателя привычки к Привычке"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitUpdateAPIView(UpdateAPIView):
    """Класс для редактирования экземпляра модели Habit (CRUD)"""
    serializer_class = HabitSerializer
    # Получаем все данне из БД
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(DestroyAPIView):
    """Класс для удаления экземпляра модели Habit (CRUD)"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitListAPIView(ListAPIView):
    """Класс для выведения всех экземпляров модели Habit (CRUD)"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)
    pagination_class = CustomPagination


class HabitRetrieveAPIView(RetrieveAPIView):
    """Класс для выведения одного экземпляра модели Habit (CRUD)"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class PublicHabitListAPIView(ListAPIView):
    """
    Класс просмотра списка всех публичных привычек (от всех Пользователей).
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # pagination_class = HabitCustomPagination
    # IsAuthenticatedOrReadOnly – только для авторизованных или всем, но для чтения
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CustomPagination

    def get_queryset(self):
        """
        Переопределение метода,
        для отображения только публичных привычек.
        """
        return Habit.objects.filter(is_public=True)
