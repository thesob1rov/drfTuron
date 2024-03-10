from django.contrib import admin
from django.urls import path, include
from .api import *
from .views import *
urlpatterns = [
    path('login/', login, name='login'),
    path('auth/', include('djoser.urls.jwt'))
]
