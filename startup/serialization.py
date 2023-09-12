from rest_framework import serializers
from .models import StartupModel, UserModel
from django.contrib.auth.models import User

class StartupSerializer(serializers.ModelSerializers):
    class Meta:
        model = StartupModel
        fields = '__all__'