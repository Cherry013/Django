from django.urls import re_path
from tutorial import views

urlpatterns = [
    re_path(r'^api/tutorial$', views.tutorial_list),
    re_path(r'^api/tutorial/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^api/tutorial/published$', views.tutorial_list_published),
]