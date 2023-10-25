from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер привычки """
    class Meta:
        """ Мета-данные """
        model = Habit
        fields = '__all__'
