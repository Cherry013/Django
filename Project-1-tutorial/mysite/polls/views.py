from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import Choice, Question

# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join(q.question_text for q in latest_question_list)
    # return HttpResponse(output)
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context,req))
    context = {"latest_question_list":latest_question_list}
    return render(req, "polls/index.html", context)

def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # return HttpResponse(f"You're looking at question { question_id }")
    return render(req, "polls/detail.html", {"question" : question})

# # above or this for view detail
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req,"polls/results.html",{"question": question})

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            req,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))