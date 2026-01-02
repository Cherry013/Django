from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView

from .models import Choice, Question

# Create your views here.
# def index(req):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # output = ", ".join(q.question_text for q in latest_question_list)
#     # return HttpResponse(output)
#     # template = loader.get_template("django-polls/index.html")
#     # return HttpResponse(template.render(context,req))
#     context = {"latest_question_list":latest_question_list}
#     return render(req, "django-polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# def detail(req, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     # return HttpResponse(f"You're looking at question { question_id }")
#     return render(req, "django-polls/detail.html", {"question" : question})

# # above or this for view detail
# def detail(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     return render(request, "django-polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(req, pk):
#     question = get_object_or_404(Question, pk=pk)
#     return render(req,"django-polls/results.html",{"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.vote = F("vote") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))