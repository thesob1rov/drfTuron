from django.contrib import admin
from django.urls import path

from .views import RegisterSubject

urlpatterns = [
    path('register_subject/', RegisterSubject.as_view(), name='register_subject'),
]
