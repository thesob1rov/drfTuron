from django.contrib import admin
from django.urls import path
from .api import *
from .views import RegisterStudent, StudentList

urlpatterns = [
    path('register_student/', RegisterStudent.as_view(), name='register_student'),
    path('students/', StudentList.as_view(), name='students')
]
