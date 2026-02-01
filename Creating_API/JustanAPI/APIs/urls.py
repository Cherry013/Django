from django.urls import path

from .views import FriendsAPI

urlpatterns = [
    path("Friends/", FriendsAPI.as_view()),
]