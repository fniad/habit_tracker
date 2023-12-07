""" Модели приложения habits """
from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):
    """ Модель привычки """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    place = models.CharField(max_length=255, blank=True, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    duration = models.DurationField(**NULLABLE, verbose_name='Длительность выполнения')
    action = models.TextField(verbose_name='Действие')
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name='Связанная привычка'
    )
    is_pleasant = models.BooleanField(default=False, **NULLABLE, verbose_name='Приятная привычка')
    is_public = models.BooleanField(default=False, verbose_name='Публичная привычка')
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Награда')
    periodicity = models.SmallIntegerField(default=1, verbose_name='Периодичность выполнения в днях')
    last_updated = models.DateField(auto_now_add=True, verbose_name='Дата и время последнего обновления')

    def __str__(self):
        return f'Действие: {self.action}, время: {self.time}, периодичность: {self.periodicity}'

    @property
    def habit_text(self):
        """ Текст привычки """
        text = f'Задача: {self.action} в {self.time}.'
        if self.place:
            text += f'Место: {self.place}.'
        if self.reward:
            text += f'Вознаграждение: {self.reward}.'
        if self.related_habit:
            text += (f'Связанная привычка: {self.related_habit.action}, '
                     f'время: {self.related_habit.time}, '
                     f'место: {self.related_habit.place}.')
        return text

    class Meta:
        """ Мета-данные """
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
