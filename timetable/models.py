from django.db import models

# Create your models here.
from classes.models import Classes
from rooms.models import Rooms
from subjects.models import Subjects


# class TimeList(models.Model):
#     lesson_count = models.CharField()
#     start = models.TimeField()
#     end = models.CharField()
#
#
# class TimeTableDay(models.Model):
#     name = models.CharField()
#
#
# class DailyTable(models.Model):
#     lesson_time = models.ForeignKey(TimeList, on_delete=models.CASCADE, blank=True, null=True)
#     room = models.ForeignKey(Rooms, on_delete=models.CASCADE, blank=True, null=True)
#     subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, null=True)
#     classs = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    # teacher = models.ForeignKey(Flows)
