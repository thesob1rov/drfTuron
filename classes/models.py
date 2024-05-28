from django.db import models

from teachers.models import Teacher
# Create your models here.


class ClassTypes(models.Model):
    class_number = models.IntegerField()
    price = models.IntegerField()


class Classes(models.Model):
    name = models.CharField(max_length=150)
    class_type = models.ForeignKey(ClassTypes, on_delete=models.CASCADE, blank=True)
    color = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True)

