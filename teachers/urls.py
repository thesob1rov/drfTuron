from django.contrib import admin
from django.urls import path

from .views import RegisterTeacher, TeacherList, TeacherProfile

urlpatterns = [
    path('register_teacher/', RegisterTeacher.as_view(), name='register_teacher'),
    path('teachers/', TeacherList.as_view(), name='teachers'),
    path('teacher-profile/<int:pk>', TeacherProfile.as_view(), name='teachers'),
]
