from rest_framework import serializers

from habits.models import Habit


class AssociatedHabitBonusValidator:
    """
    Класс валидации полей associated_habit и bonus.
    Исключение одновременного выбора связанной привычки и указания вознаграждения.
    field1 - associated_habit,
    field2 - bonus.
    """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        """Метод проверки полей на заданные параметры"""

        associated_habit = dict(value).get(self.field1)
        bonus = dict(value).get(self.field2)

        if associated_habit and bonus:
            raise serializers.ValidationError('Одновременно не допускается заполнение обоих полей: '
                                              'Выберите associated_habit или bonus')


class ExecutionDurationValidator:
    """
    Класс валидации проверки длительности выполнения задания.
    Время выполнения должно быть не больше 120 секунд.
    """
    def __init__(self, execution_duration):
        self.execution_duration = execution_duration

    def __call__(self, value):
        """
        Метод проверки поля execution_duration на соответсвие заданным параметрам.
        """
        if self.execution_duration in value:
            execution_duration = dict(value).get(self.execution_duration)
            if int(execution_duration) > 120:
                raise serializers.ValidationError('Время выполнения задания не должно превышать 120 секунд.')

        # associated_habit = dict(value).get("associated_habit")
        # execution_duration = dict(value).get(self.execution_duration)
        # if not associated_habit and not execution_duration:
        #     raise serializers.ValidationError('Длительность выполнения Полезной привычки обязательный атрибут')


class AssociatedHabitValidator:
    """
    Класс валидации полей is_pleasant_habit у связанной привычки
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """
        Метод проверки полей is_pleasant_habit и associated_habit на соответсвие заданным параметрам.
        """
        associated_habit = dict(value).get(self.field)

        if associated_habit and not associated_habit.is_pleasant_habit:
            raise serializers.ValidationError('В связанные привычки могут попадать только привычки '
                                              'с признаком приятной привычки.')


class IsPleasantHabitBonusValidator:
    """
    Класс валидации полей is_pleasant_habit и bonus.
    У приятной привычки не может быть вознаграждения или связанной привычки..
    """

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        """
        Метод проверки полей is_pleasant_habit и associated_habit на соответсвие заданным параметрам.
        """
        associated_habit = dict(value).get("associated_habit")
        is_pleasant_habit = dict(value).get(self.field1)
        bonus = dict(value).get(self.field2)

        if bonus is not None and is_pleasant_habit is True:
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения.')

        if is_pleasant_habit and associated_habit:
            raise serializers.ValidationError('У приятной привычки не может быть признака связанной привычки.')


class PeriodicityValidator:
    """
    Класс валидации поля периодичности (periodicity) выполнения привычки.
    """

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        if self.periodicity in value:
            periodicity = dict(value).get(self.periodicity)
            if int(periodicity) > 7:
                raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

        # associated_habit = dict(value).get("associated_habit")
        # periodicity = dict(value).get(self.periodicity)
        # if not associated_habit and not periodicity:
        #     raise serializers.ValidationError('Периодичность выполнения Полезной привычки обязательный атрибут')
