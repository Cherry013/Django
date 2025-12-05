from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("index", views.index, name="index"),
    path("<int:rollno>/Student/", views.Stu, name="Student"),
    path("<int:id>/Teacher/", views.Teach, name="Teacher"),
    path("total", views.total, name="total"),
    path("time",views.time, name="time"),
]