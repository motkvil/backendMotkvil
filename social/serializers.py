from rest_framework import serializers
from .models import SocialNetwork



class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('id','title','link','created', 'updated')
        read_only_fields = ('created', 'updated',)
