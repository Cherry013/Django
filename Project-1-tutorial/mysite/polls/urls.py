from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),    # ex: /polls/21/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),  # ex: /polls/25/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),    #ex: /polls/26/vote
]