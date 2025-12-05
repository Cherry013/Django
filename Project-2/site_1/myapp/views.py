from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Student, Teacher

# Create your views here.
def index(req):
    return HttpResponse("!Hello, How areyou")

def Stu(req,rollno):
    obj = Student.objects.get(rollno=rollno)
    # return HttpResponse(f"Details: <br> Student Name: {obj.name} <br> Roll_Number: {obj.rollno} <br> Section: {obj.classSection}")
    return render(req,"myapp/student.html",{"obj":obj})

def Teach(req,id):
    obj = Teacher.objects.get(pk=id)
    # return HttpResponse(f"Details: <br> Teacher Name: {obj.name} <br> Section: {obj.classSection}")
    return render(req,"myapp/teacher.html",{"obj":obj})

def total(req):
    obj = Student.objects.all()
    return render(req,"myapp/total.html",{"obj":obj})

def time(req):
    c_time = timezone.now() # Date Time upto microseconds
    k = timezone.localtime(c_time).time() # eg 10:25:15.3549165 # localtime() used to get the time of your location from settings
    k = list(str(k).split('.')) #["10:25:15","3549165"]
    k = k[0] # 10:25:15
    st = f"Date: {c_time.date()} <br> Time: {k}"
    return HttpResponse(st)