from django.urls import path
from .api import SocialViewset, NewsView, ViewsView, ViewVisit

urlpatterns = [
    path('', SocialViewset.as_view()),
    path('news/', NewsView.as_view()),
    path('views/', ViewsView.as_view()),
    path('visit/', ViewVisit.as_view()),
]

