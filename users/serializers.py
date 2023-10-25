""" Сериалайзеры для users """
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериалайзер пользователя """
    class Meta:
        """ Мета-данные """
        model = User
        fields = '__all__'


class UserPublicProfileSerializer(serializers.ModelSerializer):
    """ Сериалайзер публичной информации о пользователе """
    class Meta:
        """ Мета-данные """
        model = User
        fields = ('username', 'first_name')


class UserProfileSerializer(serializers.ModelSerializer):
    """ Сериалайзер личной информации о пользователе """
    class Meta:
        """ Мета-данные """
        model = User
        fields = ('__all__')



class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериалайзер создания пользователя """
    class Meta:
        """ Мета-данные """
        model = User
        fields = ('email', 'username', 'password')
