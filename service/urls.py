from django.urls import path
from .api import ServiceView, MyServicesView

urlpatterns = [
    path('', ServiceView.as_view()),
    path('my/', MyServicesView.as_view())
]
