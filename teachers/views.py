from django.shortcuts import render

from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from students.permissions import IsAdmin

from users.models import CustomUser
from .models import Teacher
from subjects.models import Subjects

import jwt
import json

from drfTuron.settings import SECRET_KEY
from .serializers import TeacherSerializer


class RegisterTeacher(APIView):
    authentication_classes = (TokenAuthentication,)

    # permission_classes = [IsAdmin, ]

    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)[7:]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get("user_id")
        user = CustomUser.objects.get(pk=user_id)
        status = IsAdmin(user)
        if status.is_user_admin():
            data = json.loads(request.body)
            user = CustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                number=data['number'],
                role='student'
            )
            user.save()
            print(data)
            subject = Subjects.objects.get(name=data['subject']['name'])
            print(subject)
            teacher = Teacher(user_id=user.id, subject_id=subject.id)
            teacher.save()
            return Response({'post': data})
        else:
            return Response({'post': "Sani aqlingamas"})


class TeacherList(APIView):
    def get(self, request):
        data = Teacher.objects.all()
        serializer = TeacherSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(request.body)

        if data['subject'] == 'all':
            data = Teacher.objects.all()
            serializer = TeacherSerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = Teacher.objects.filter(subject__name=data['subject'])
            serializer = TeacherSerializer(data, many=True)
            return Response(serializer.data)


class TeacherProfile(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
