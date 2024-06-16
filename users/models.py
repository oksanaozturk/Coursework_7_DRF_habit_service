from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Класс для создания модели Пользователя"""

    username = None

    email = models.EmailField(
        max_length=150, unique=True, verbose_name="email", help_text="Введите email"
    )
    # Необходимо добавить библиотеку через команду pip install "django-phonenumber-field[phonenumberslite]"
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Укажите Ваш номер телефона",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users_avatar",
        verbose_name="Аватар пользователя",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    counter = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Введите страну проживания",
        **NULLABLE
    )

    # Выбираем полем для авторизации email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользоаптель"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
