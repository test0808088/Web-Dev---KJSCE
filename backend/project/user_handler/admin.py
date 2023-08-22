from django.contrib import admin
from .models import Faculty, Staff, Student, Course, CourseAssignment

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['branch','dept','employee_code','faculty_name','employee_abbreviation','faculty_email','experience','post']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['branch', 'employee_abbreviation', 'staff_name', 'staff_email', 'experience', 'post']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_branch', 'student_name', 'roll_number', 'email', 'proctor', 'student_contact_no', 'parents_contact_no', 'parent_email_id']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['branch', 'course_code', 'course_name', 'dept', 'sem', 'scheme_name', 'credit', 'hours']

class CourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'assigned_by')

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseAssignment, CourseAssignmentAdmin)
