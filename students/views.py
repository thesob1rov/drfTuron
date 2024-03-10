from django.shortcuts import render
from users.models import CustomUser

from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import permissions
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters

import jwt
import json

from drfTuron.settings import SECRET_KEY
from students.permissions import IsAdmin
from students.models import Student
from students.serializers import StudentSerializer


class RegisterStudent(APIView):
    authentication_classes = (TokenAuthentication,)

    # permission_classes = [IsAdmin, ]
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)[7:]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get("user_id")
        user = CustomUser.objects.get(pk=user_id)
        status = IsAdmin(user)
        if status.is_user_admin():
            print("True")
            data = json.loads(request.body)
            user = CustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                number=data['number'],
                role=data['role']
            )
            user.save()
            student = Student(user_id=user.id)
            student.save()
            return Response({'post': data})
        else:
            return Response({'post': "Sani aqlingamas"})


class StudentList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class FilteredNewStudentList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    # def post(self):

    def get_queryset(self):
        queryset = Student.objects.all()
        # class_number = self.