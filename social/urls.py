from django.urls import path
from .api import SocialViewset

urlpatterns = [
    path('', SocialViewset.as_view()),
]