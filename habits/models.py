""" Модели приложения habits """
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
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

    def str(self):
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

    def clean(self):
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError('Связанная привычка должна быть приятной')

    def clean(self):
        super().clean()
        if self.duration and self.duration > timezone.timedelta(minutes=2):
            raise ValidationError('Время на выполнение больше 2 минут.')

    class Meta:
        """ Мета-данные """
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        models.CheckConstraint(
            check=models.Q(duration__lte=timezone.timedelta(minutes=2)),
            name='duration_max_constraint'
        )
