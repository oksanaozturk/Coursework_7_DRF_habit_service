from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}

PERIOD_CHOICES = [
    (1, "Ежедневно"),
    (2, "Каждые 2 дня"),
    (3, "Каждые 3 дня"),
    (4, "Каждые 4 дня"),
    (5, "Каждые 5 дней"),
    (6, "Каждые 6 дней"),
    (7, "Еженедельно"),
]


class Habit(models.Model):
    """
    Класс Привычки и его свойства.
    is_pleasant_habit - Указывается только для Приятной привычки.
    associated_habit - указывается только для Полезной привычки.
    """

    owner = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name="habits",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=256,
        verbose_name="Место",
        help_text="Ввведите место выполнения привычки",
        **NULLABLE
    )
    time = models.TimeField(
        verbose_name="Время",
        help_text="Введите время выполнения привычки"
    )
    action = models.CharField(
        max_length=256,
        verbose_name="Действие",
        help_text="Введите действие, которое нужно выполнить",
    )
    is_pleasant_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    # Ещё один вариант написания associated_habit = models.ForeignKey("self"). Ссылка на эту же модель.
    associated_habit = models.ForeignKey(
        "Habit",
        verbose_name="Связанная приятная привычка",
        on_delete=models.SET_NULL,
        help_text="Данные признак указывается только для Полезной привычки, "
        "если есть связанная с ней, Приятная привычка",
        **NULLABLE
    )
    periodicity = models.PositiveIntegerField(
        verbose_name="Периодичность выполнения",
        choices=PERIOD_CHOICES,
        help_text="Введите периодичность выполнения привычки для напоминания, "
        "1 раз в каждые сколько дней.",
        **NULLABLE
    )
    bonus = models.CharField(
        max_length=256,
        help_text="Напишите, какое будет вознаграждение за выполнения "
        "Полезной привычки",
        verbose_name="Вознаграждение",
        **NULLABLE
    )
    execution_duration = models.PositiveIntegerField(
        verbose_name="Длительность выполнения",
        help_text="Сколько потребуется "
        "времени на выполнение "
        "Полезной привычки "
        "(в секундах).",
        **NULLABLE
    )
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.owner} будет делать {self.action} в {self.time} в {self.place}"
