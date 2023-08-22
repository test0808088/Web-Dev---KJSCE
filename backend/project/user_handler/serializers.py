from rest_framework import serializers
from .models import Student, Faculty, Staff, Course, CourseAssignment




class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

# class StudentSerializer(serializers.ModelSerializer):
#     proctor = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), allow_null=True, required=False)

#     class Meta:
#         model = Student
#         fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    proctor = FacultySerializer(read_only=True)  # Use the FacultySerializer for read-only display

    class Meta:
        model = Student
        fields = '__all__'

class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'





class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseAssignmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())  # Use the Faculty model queryset

    class Meta:
        model = CourseAssignment
        fields = '__all__'