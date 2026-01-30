from django.urls import path
from .views import Registger
urlpatterns = [
    path('register', Registger.as_view())
]