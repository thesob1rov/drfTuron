from django.contrib import admin
from django.urls import path

from .views import CreatRoomAndList, RoomProfile

urlpatterns = [
    path('rooms/', CreatRoomAndList.as_view(), name='rooms'),
    path('room-profile/<int:pk>/', RoomProfile.as_view(), name='room_profile')
]
