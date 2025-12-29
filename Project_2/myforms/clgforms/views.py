from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Section, Students


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def section(request,sec_id):
    x = Section.objects.get(pk=sec_id)
    return HttpResponse(f"<h1>Sections</h1><br> <h3> Section Name : {x.SectionName}<h3><br> Teacher Name : {x.Sec_Teacher} <h3></h3>")

def Sec_details(request):
    x = Section.objects.all()
    return render(request, "clgforms/sec_details.html", {"sec": x})

def student_details(request, sec_id):
    x = get_object_or_404(Section, pk=sec_id)
    sec = x.students_set.all()
    return render(request, "clgforms/StudentDetails.html", {"sec": sec, "sec_name":x})

def Section_choice(request):
    pass

def Student_form(request, sec_id):
    x = Section.objects.get(pk=sec_id)
    return render(request,"clgforms/StudentForm.html", {"sec_id":sec_id, "x":x})

def insert_student(request,sec_id):
    try:
        x = get_object_or_404(Section, pk=sec_id)
        Selected = x.students_set.create(StudentName=request.POST["StudentName"], StudentID=request.POST["StudentID"])
    except (KeyError, Students.DoesNotExist) as e:
        return HttpResponse(f"<h1>Cannot be created or Does not Existed</h1> <br> {e}")
    except Exception as ex:
        return HttpResponse(f"{ex}")
    else:
        Selected.save()
        return HttpResponseRedirect(reverse("clgforms:student_details",args=(sec_id,)))

