from django.contrib import admin

# Register your models here.

from .models import Faculty, Staff, Student, Course

class FacultyAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Faculty._meta.get_fields()]
    list_display = ['employee_abbreviation', 'branch', 'dept', 'employee_code', 'faculty_name', 'faculty_email', 'experience', 'post']

class StaffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Staff._meta.get_fields()]
    

class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.get_fields()]
    

class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.get_fields()]


admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
