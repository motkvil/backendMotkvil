from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        read_only_fields = ('created', 'updated',)

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password','email')
