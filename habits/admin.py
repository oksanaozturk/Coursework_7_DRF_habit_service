from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Класс для регистрации User в админке."""

    list_display = (
        "id",
        "owner",
        "place",
        "time",
        "action",
        "is_pleasant_habit",
        "associated_habit",
        "periodicity",
        "bonus",
        "execution_duration",
        "is_public",
    )
    list_filter = ("owner",)
    search_fields = ("owner", "action")
