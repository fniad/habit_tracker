""" Валидаторы приложения habits """
from rest_framework.serializers import ValidationError
from datetime import timedelta
from django.utils import timezone

class HabitOrRewardValidator:
    """ Валидатор для выбора или связанной привычки, или вознаграждения """

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, values):
        related_habit = values.get(self.related_habit)
        reward = values.get(self.reward)

        if related_habit and reward:
            raise ValidationError({
                self.related_habit: 'При выборе связанной привычки нельзя указывать вознаграждение.',
                self.reward: 'При выборе вознаграждения нельзя указывать связанную привычку.'
            })


class HabitTimeValidator:
    """ Валидатор времени выполнения привычки """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_duration = value.get(self.field)
        if time_duration:
            if time_duration > timedelta(seconds=120):
                raise ValidationError(
                    {self.field: ['Время выполнения привычки должно быть не больше 120 секунд.']}
                )


class RelatedHabitValidator:
    """ Валидатор связанной привычки """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)

        if related_habit:
            if not related_habit.is_pleasant:
                raise ValidationError(
                    {self.field: ['Связанная привычка должна быть приятной.']}
                )


class PleasantHabitValidator:
    """ Валидатор приятной привычки """

    def __init__(self, is_pleasant, reward, related_habit):
        self.is_pleasant = is_pleasant
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        is_pleasant = value.get(self.is_pleasant)
        reward = value.get(self.reward)
        related_habit = value.get(self.related_habit)

        if is_pleasant and (reward or related_habit):
            raise ValidationError(
                {self.is_pleasant: ['Приятная привычка не может иметь вознаграждения или связанных привычек.']}
            )


class HabitFrequencyValidator:
    """ Валидатор периодичности выполнения привычки """
    def __init__(self, periodicity):
        self.field = periodicity

    def __call__(self, value):
        periodicity = value.get(self.field)
        if periodicity:
            if periodicity > 7:
                raise ValidationError(
                    {self.field: [
                        'Нельзя выполнять привычку реже, чем 1 раз в 7 дней!']}
                )
