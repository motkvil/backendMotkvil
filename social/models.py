from django.db import models

# Create your models here.
class SocialNetwork(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)