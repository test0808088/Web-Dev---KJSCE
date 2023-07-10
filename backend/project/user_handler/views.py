from django.shortcuts import render
from . import models
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers

# Create your views here.

class facultyViewSet(viewsets.ModelViewSet):
    queryset = models.faculty.objects.all()
    serializer_class = serializers.faculty_serializer 

    def put(self, request, id=None):
        faculty = models.faculty.objects.all()
        serializer = serializers.faculty_serializer(faculty, data = request.data)
        return Response(serializer.data)


class staffViewSet(viewsets.ModelViewSet):
    queryset = models.staff.objects.all()
    serializer_class = serializers.staff_serializer

    def put(self, request, id=None):
        staff = models.staff.objects.all()
        serializer = serializers.staff_serializer(staff, data = request.data)
        return Response(serializer.data)
