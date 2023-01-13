from django.urls import path
from .api import HelloMyPet

urlpatterns = [
    path('',HelloMyPet.as_view())
]
