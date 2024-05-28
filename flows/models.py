from django.db import models

from students.models import Student
from subjects.models import Subjects
from teachers.models import Teacher


class FlowTypes(models.Model):
    classes = models.CharField()
    color = models.CharField()
    start = models.IntegerField()
    end = models.IntegerField()


class Flow(models.Model):
    name = models.CharField()
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    students = models.ManyToManyField(Student)
