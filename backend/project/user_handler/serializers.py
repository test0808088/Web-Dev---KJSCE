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

class CourseAllotmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseAllotment
        fields = '__all__'

class StudentAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAchievement
        fields = '__all__'

class AdminCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdminCredentials
        fields = '__all__'

class SubAdminCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubAdminCredentials
        fields = '__all__'


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AcademicYear
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marks
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'