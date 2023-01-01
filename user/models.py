from django.db import models

# Create your models here.

class CustomUser(models.Model):

    active = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.active