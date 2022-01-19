from dataclasses import field
from distutils import dep_util
from webbrowser import get
from rest_framework import serializers
from project.models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email',)
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = "__all__"
        depth = 1

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = "__all__"
        depth = 1