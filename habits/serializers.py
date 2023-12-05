from rest_framework import serializers
from habits.models import Habit
from habits.validators import HabitOrRewardValidator, HabitTimeValidator, RelatedHabitValidator, PleasantHabitValidator, \
    HabitFrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер привычки """
    class Meta:
        """ Мета-данные """
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'duration', 'action', 'related_habit', 'is_pleasant', 'is_public',
                  'reward', 'periodicity', 'last_updated')
        read_only_fields = ('user', 'last_updated',)
        validators = [
            HabitOrRewardValidator('related_habit', 'reward'),
            HabitTimeValidator('duration'),
            RelatedHabitValidator('related_habit'),
            PleasantHabitValidator('is_pleasant', 'reward', 'related_habit'),
            HabitFrequencyValidator('periodicity')
        ]
