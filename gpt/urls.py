from django.urls import path
from .views import gptChat

urlpatterns = [
  path('gpt/', gptChat.as_view()),
]
