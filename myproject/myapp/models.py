from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=264)
    address=models.CharField(max_length=264)
    course=models.CharField(max_length=264)
    objects=models.Manager()

