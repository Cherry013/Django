from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("specifics/<int:question_id>/", views.detail, name="detail"),    # ex: /polls/21/
    path("<int:question_id>/results/", views.results, name="results"),  # ex: /polls/25/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),    #ex: /polls/26/vote
]