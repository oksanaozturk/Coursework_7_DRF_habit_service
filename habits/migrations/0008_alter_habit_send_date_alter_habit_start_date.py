# Generated by Django 5.0.6 on 2024-06-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0007_rename_send_next_date_habit_send_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="send_date",
            field=models.DateField(
                auto_now=True,
                null=True,
                verbose_name="Следующая дата выполнения привычки",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="start_date",
            field=models.DateField(
                auto_now=True,
                help_text="Введите дату начала Полезной привычки",
                null=True,
                verbose_name="Дата старта",
            ),
        ),
    ]