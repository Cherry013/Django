from datetime import timezone

from django.db import models

# Create your models here.
class Friends(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    Pno = models.IntegerField(unique=True)
    email = models.EmailField()
    Description = models.TextField(default='Friends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.name} : {self.Description}"

    def __repr__(self):
        return self.name