from django.db import models
from user.models import CustomUser

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    teachers = models.ManyToManyField(CustomUser, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
