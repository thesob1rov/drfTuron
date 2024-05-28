# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers

from students.models import Student
from users.models import CustomUser
from classes.serializers import ClassSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'first_name', 'last_name', 'number', 'image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image=validated_data['image'],
            number=validated_data['number'],
        )
        print(validated_data)
        # user = User.objects.create(**validated_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
    # online userni srazu tushurib berishi uchun
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'role', 'birth_date', 'image', 'parent_name',
                  'number', 'age']


class StudentSerializer(serializers.ModelSerializer):
    # online userni srazu tushurib berishi uchun
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = UserListSerializer(read_only=True)
    classes = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['user', 'user', 'classes']
