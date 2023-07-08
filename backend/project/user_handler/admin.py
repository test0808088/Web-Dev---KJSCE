from django.contrib import admin

# Register your models here.

from .models import Branch, Faculty, Staff, Student, Course, Year

admin.site.register(Branch)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Year)