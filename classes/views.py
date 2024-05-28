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

from .models import ClassTypes, Classes
from students.models import Student
from .serializers import ClassTypesSerializer, ClassSerializer
from students.serializers import StudentSerializer


class ClassesList(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body)
        print(data)
        post_type = data.get('post_type')
        if post_type == 'create':
            serializer = ClassSerializer(data=json.loads(request.body))
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data': serializer.data})
        if post_type == 'filter':
            class_type_id = data.get('class_type_id')
            color = data.get('color')
            class_data = Class.objects.filter(class_type_id=class_type_id, color=color)
            serializers = ClassSerializer(class_data, many=True)
            print(class_type_id, color)
            return Response({"data": serializers.data})


class ClassProfile(generics.RetrieveUpdateAPIView):
    queryset = Classes
    serializer_class = ClassSerializer
    authentication_classes = (TokenAuthentication,)


class JoinClassWithStudents(APIView):
    def post(self, request):
        data = json.loads(request.body)
        students = data.get('students')
        class_id = data.get('class_id')
        Student.objects.filter(id__in=students).update(student_class_id=class_id)
        students = Student.objects.filter(id__in=students)
        serializers = StudentSerializer(students, many=True)
        return Response({'data': serializers.data})

    def get(self):
        return Response()


class CreatClassWithStudents(APIView):
    def post(self, request):
        data = json.loads(request.body)
        students = data.get('students')
        class_data = data.get('class')
        teacher = data.get('teacher')
        print(data)
        student_class = Classes.objects.create(name=class_data.get('name'), class_type_id=class_data.get('class_type_id'),
                                             color=class_data.get('color'), teacher_id=teacher.get('id'))
        Student.objects.filter(id__in=students).update(student_class_id=student_class.id)
        students = Student.objects.filter(id__in=students)
        serializers = StudentSerializer(students, many=True)
        return Response({'data': serializers.data})

    def get(self):
        return Response()


class RemoveStudentsFromClass(APIView):
    def post(self, request):
        data = json.loads(request.body)
        students = data.get('students')
        class_id = data.get('class_id')
        Student.objects.filter(id__in=students).update(student_class_id=None)


