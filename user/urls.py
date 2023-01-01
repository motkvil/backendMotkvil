from django.urls import path
from .api import UserViewset

urlpatterns = [
    path('', UserViewset.as_view()),
]