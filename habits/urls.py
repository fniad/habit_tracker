""" URLs training_courses """
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import *

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = HabitsConfig.name

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = ([
    path('habit/', HabitListAPIView.as_view(), name='list-habits'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='view-habit'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='create-habit'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update-habit'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete-habit'),
    path('habit/public/', ListPublicHabits.as_view(), name='list-public-habits'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
])
