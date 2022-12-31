from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):

  email = models.EmailField(unique=True)
  color = models.TextField(max_length=200, blank=True)
  image = models.URLField(blank=True)


  def __str__(self):
      return self.username
  