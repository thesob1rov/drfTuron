from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, viewsets
# Create your views here.

from .models import Rooms

from .serializers import RoomSerializer


class CreatRoomAndList(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer


class RoomProfile(generics.RetrieveUpdateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer

