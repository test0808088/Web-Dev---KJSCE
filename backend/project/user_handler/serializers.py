from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

class faculty_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.faculty
        fields = '__all__'

class staff_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.staff
        fields = '__all__'