from rest_framework import serializers
from .models import StartupModel, UserModel
from django.contrib.auth.models import User

class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'user_price']
        