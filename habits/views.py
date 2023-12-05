""" Представления для привычек"""
from rest_framework import generics
from .models import Habit
from .pagination import HabitPagination
from .serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """ Список уроков """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('pk')
    pagination_class = HabitPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Подробная информация об уроке """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('pk')


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание урока """
    serializer_class = HabitSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Обновление урока """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('pk')


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление урока """
    queryset = Habit.objects.all().order_by('pk')
