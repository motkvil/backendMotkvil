from django.db import models
from user.models import CustomUser
# Create your models here.
class SocialNetwork(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NewsModel(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ViewsModel(models.Model):
    title = models.CharField(max_length=100, default='Vista')
    user = models.ManyToManyField(CustomUser, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


