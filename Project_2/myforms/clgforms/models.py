from django.db import models



# Create your models here.
class Section(models.Model):
    id = models.AutoField(primary_key=True)
    SectionName = models.CharField(max_length=3)
    Sec_Teacher = models.CharField(max_length=200)
    S_Year = models.IntegerField()

    def __str__(self):
        return f"{self.SectionName}"

    def __repr__(self):
        return f"{self.SectionName}"

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=200)
    StudentID = models.IntegerField(unique=True)
    Sec_Name = models.ForeignKey(Section, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.StudentName}"

    def __repr__(self):
        return f"{self.StudentName}"