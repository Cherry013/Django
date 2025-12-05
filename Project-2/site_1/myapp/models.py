from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    classSection = models.CharField(max_length=1)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    classSection = models.CharField(max_length=1)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name