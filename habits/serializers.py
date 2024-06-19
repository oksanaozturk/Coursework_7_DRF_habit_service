from rest_framework import serializers

from habits.models import Habit
from habits.validators import AssociatedHabitBonusValidator, ExecutionDurationValidator, AssociatedHabitValidator, \
     IsPleasantHabitBonusValidator, PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
                      AssociatedHabitBonusValidator("associated_habit", "bonus"),
                      ExecutionDurationValidator("execution_duration"),
                      AssociatedHabitValidator("associated_habit"),
                      IsPleasantHabitBonusValidator("is_pleasant_habit", "bonus"),
                      PeriodicityValidator("periodicity"),
                      ]
