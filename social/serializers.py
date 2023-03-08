from rest_framework import serializers
from .models import SocialNetwork, ViewsModel,NewsModel, VisitModel



class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ('id','title','link','created', 'updated')
        read_only_fields = ('created', 'updated',)

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ('id','title','description','created', 'updated')
        read_only_fields = ('created', 'updated',)

class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewsModel
        fields = ('id','title','user','created', 'updated')
        read_only_fields = ('created', 'updated',)

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitModel
        fields = ('__all__')
        read_only_fields = ('created', 'updated',)



