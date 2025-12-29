from django.urls import path
from . import views

app_name = 'clgforms'

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.Sec_details, name='details'),
    path("<int:sec_id>/students", views.student_details, name='student_details'),
    path("<int:sec_id>/stuforms", views.Student_form, name="Student_form"),
    path("<int:sec_id>/create", views.insert_student, name='insert_student'),
]