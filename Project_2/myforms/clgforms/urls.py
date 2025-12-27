from django.urls import path
from . import views

app_name = 'clgforms'

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<int:sec_id>', views.section, name='section'),
    path('details', views.Sec_details, name='details'),
    path("<int:s_id>/students", views.student_details, name='student_details'),
]