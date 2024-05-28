from django.db import models

from teachers.models import Teacher


# Create your models here.


class Rooms(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=150)
