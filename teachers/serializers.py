# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Teacher
# from students.serializers import UserSerializer
from users.models import CustomUser

from subjects.serializers import SubjectSerializer


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'role', 'birth_date', 'image', 'parent_name',
                  'number', 'age']


class TeacherSerializer(serializers.ModelSerializer):
    # online userni srazu tushurib berishi uchun
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = UserListSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject']
