from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Класс для создания экземпляра модели User (CRUD)"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # Делаем разрешение для этого контроллера, чтобы незарегистрированный пользователь имел доступ к регистрации
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Данный метод необходим для того, чтобы нам не мешала настройка 'username = None',
        указанная нами в модели User в models.py"""
        user = serializer.save(is_active=True)
        # Кешируем обязательно пароль Пользователя
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """Класс для редактирования экземпляра модели User (CRUD)"""

    serializer_class = UserSerializer
    # Получаем все данне из БД
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserDestroyAPIView(DestroyAPIView):
    """Класс для удаления экземпляра модели User (CRUD)"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserListAPIView(ListAPIView):
    """Класс для выведения всех экземпляров модели User (CRUD)"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserRetrieveAPIView(RetrieveAPIView):
    """Класс для выведения одного экземпляра модели User (CRUD)"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
