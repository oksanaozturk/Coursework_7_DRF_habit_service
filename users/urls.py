from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    # Путь для вывода страницы со всеми объектами модели User
    path("users-list/", UserListAPIView.as_view(), name="users-list"),
    # Путь для вывода страницы с одним объектом модели User
    path("user-view/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-retrieve"),
    # Путь для вывода страницы при создании нового объекта модели User
    path("user-create/", UserCreateAPIView.as_view(), name="user-create"),
    # Путь для редактирования объекта модели User
    path("user-update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    # Путь для удаления объекта модели User
    path("user-destroy/<int:pk>/", UserDestroyAPIView.as_view(), name="user-destroy"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
