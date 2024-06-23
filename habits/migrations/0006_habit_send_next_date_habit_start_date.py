# Generated by Django 5.0.6 on 2024-06-23 08:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0005_alter_habit_execution_duration_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="send_next_date",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Следующая дата выполнения привычки",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="start_date",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                help_text="Введите дату начала Полезной привычки",
                null=True,
                verbose_name="Дата старта",
            ),
        ),
    ]