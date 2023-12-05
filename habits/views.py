""" Представления для привычек"""
from rest_framework import generics
from .models import Habit
from .pagination import HabitPagination
from .permissions import IsOwnerOrSuperuser
from .serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """ Список уроков """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('pk')
    pagination_class = HabitPagination
    permission_classes = [IsOwnerOrSuperuser]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Подробная информация об уроке """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('pk')
    permission_classes = [IsOwnerOrSuperuser]


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание урока """
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrSuperuser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Обновление урока """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('pk')
    permission_classes = [IsOwnerOrSuperuser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление урока """
    queryset = Habit.objects.all().order_by('pk')
    permission_classes = [IsOwnerOrSuperuser]


class ListPublicHabits(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
