from .models import Classes, ClassTypes

from rest_framework import serializers
from teachers.serializers import TeacherSerializer


class ClassTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTypes
        fields = ['id', 'class_number', 'price']


class ClassSerializer(serializers.ModelSerializer):
    class_type = ClassTypesSerializer()
    teacher = TeacherSerializer()

    # students = StudentSerializer()

    class Meta:
        model = Classes
        fields = ['id', 'name', 'class_type_id', 'class_type', 'color', 'teacher_id', 'teacher']

    def create(self, validated_data):
        class_type_data = validated_data.pop('class_type')
        filtered_class = ClassTypes.objects.get(class_number=class_type_data['class_number'])
        instance = Classes.objects.create(
            class_type_id=filtered_class.pk,
            color=validated_data['color'],
            name=validated_data['name']
        )
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.color = validated_data.get("color", instance.color)
        class_type_data = validated_data.pop('class_type')
        filtered_class = ClassTypes.objects.get(class_number=class_type_data['class_number'])
        instance.class_type = filtered_class
        instance.save()
        return instance
