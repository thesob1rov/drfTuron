from django.conf import settings

from rest_framework import serializers
from teachers.serializers import TeacherSerializer
from .models import Rooms
from teachers.models import Teacher


class RoomSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer(required=True)

    class Meta:
        model = Rooms
        fields = ['id', 'name', 'teacher']

    def create(self, validated_data):
        print(validated_data)
        teacher_data = validated_data.pop('teacher')
        teacher_instance = Teacher.objects.get(pk=teacher_data['id'])
        instance = Rooms.objects.create(
            teacher=teacher_instance,
            name=validated_data['name']
        )
        return instance

    def update(self, instance, validated_data):
        print(validated_data)
        instance.name = validated_data.get("name", instance.name)
        instance.teacher = validated_data.get('teacher', instance.teacher)
        print(instance.teacher)
        serializer = TeacherSerializer(instance.teacher)
        print(serializer.data)
        instance.save()
        info = {
            "room": instance,
            "teacher": serializer.data
        }

        return instance, serializer.data

