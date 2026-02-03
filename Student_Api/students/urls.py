from django.urls import path

from .views import *

urlpatterns = [
    path("students/all_details", StudentAPIView.as_view()),
    path("students/create", StudentAPIView.as_view()),
    path("students/<int:pk>/", StudentDetailAPIView.as_view()),
    path("students/RUD/<int:pk>/", StudentRUDView.as_view()),
]