from django.conf import settings

from rest_framework import serializers

from students.serializers import StudentSerializer
from subjects.serializers import SubjectSerializer
from teachers.serializers import TeacherSerializer
from .models import FlowTypes, Flow
from teachers.models import Teacher
from rooms.models import Rooms
from students.models import Student


class FlowTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowTypes
        fields = '__all__'


class FlowSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Flow
        fields = ['id', 'name', 'subject', 'teacher', 'students']


class CreatFlowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flow
        fields = ['id', 'name', 'subject', 'teacher', 'students']

    def create(self, validated_data):
        print(validated_data)
        students_data = validated_data.pop('students')
        instance = Flow.objects.create(
            teacher=validated_data['teacher'],
            name=validated_data['name'],
            subject=validated_data['subject']
        )
        for student_data in students_data:
            student = Student.objects.get(id=student_data.id)
            instance.students.add(student)
        return instance
