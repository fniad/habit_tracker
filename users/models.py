""" Модели приложения users """
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя """
    is_staff = models.BooleanField(default=False)
    chat_id = models.CharField(verbose_name='ID чата', max_length=255, **NULLABLE)

    def __str__(self):
        return f"{self.username} - {self.chat_id}"

    class Meta:
        """ Мета-данные """
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
