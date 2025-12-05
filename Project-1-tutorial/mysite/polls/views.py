from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader


from .models import Question

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
    # response = "You're looking at the results of question %s"
    # return HttpResponse(response %question_id)
    return HttpResponse(f"You're looking at the results of question { question_id }")

def vote(req, question_id):
    return HttpResponse(f"You're Voting on a question { question_id }")