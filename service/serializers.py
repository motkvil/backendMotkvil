from .models import Service
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','title','description','teachers','created','updated')
        read_only_fields = ('created', 'updated') 
