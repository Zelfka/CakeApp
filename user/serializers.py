from .models import MyUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email','phone', 'city']


class MyUserRequestRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']


class MyUserResponseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['pk', 'username', 'email']


class ProfileResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'street', 'city', 'zip_code', 'last_login', 'date_joined']
