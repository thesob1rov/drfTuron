from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from users.models import CustomUser
from students.permissions import IsAdmin
from teachers.models import Teacher

import jwt
import json

from drfTuron.settings import SECRET_KEY

from .models import Subjects
from .serializers import SubjectSerializer


class RegisterSubject(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
