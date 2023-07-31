from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
        depth = 1

class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
        



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'