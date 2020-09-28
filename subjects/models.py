from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    subject1=models.CharField(max_length=100)
    subject2=models.CharField(max_length=100)
    subject3=models.CharField(max_length=100)
    subject4=models.CharField(max_length=100)
    subject5=models.CharField(max_length=100)
    subject6=models.CharField(max_length=100)

    def __str__(self):
        return self.name;