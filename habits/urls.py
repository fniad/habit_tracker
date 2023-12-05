""" URLs training_courses """
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import *

app_name = HabitsConfig.name


urlpatterns = ([
                  path('habit/', HabitListAPIView.as_view(), name='list-habits'),
                  path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='view-habit'),
                  path('habit/create/', HabitCreateAPIView.as_view(), name='create-habit'),
                  path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update-habit'),
                  path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete-habit'),
                  path('habit/public/', ListPublicHabits.as_view(), name='list-public-habits'),
              ])
