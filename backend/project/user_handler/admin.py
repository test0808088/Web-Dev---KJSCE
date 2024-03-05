from django.contrib import admin

from .models import Faculty, Staff, Student, Course,CourseAllotment,StudentAchievement,AdminCredentials, SubAdminCredentials, AcademicYear, Marks, Attendance

class FacultyAdmin(admin.ModelAdmin):
    list_display = [
        'dept', 'employee_code', 'faculty_abbreviation', 'faculty_name', 'faculty_email',
        'experience', 'post', 'mobile_number', 'display_courses_taught'
    ]

    def display_courses_taught(self, obj):
        courses_taught = CourseAllotment.objects.filter(faculty_abbreviation=obj)
        return ', '.join([f"{course.course_code} - {course.course_name}" for course in courses_taught])

    display_courses_taught.short_description = 'Courses Taught'

class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'dept', 'employee_code', 'staff_abbreviation', 'staff_name', 'staff_email',
        'experience', 'post', 'mobile_number'
    ]


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'student_branch', 'student_name', 'roll_number', 'email',
        'proctor_abbreviation', 'student_contact_no', 'parents_contact_no',
        'parent_email_id', 'year', 'session', 'course_1','course_2', 'course_3', 'course_4', 'course_5', 'course_6', 'course_7', 'course_8', 'course_9', 'course_10', 'course_11', 'course_12', 'course_13', 'course_14', 'course_15'
    ]

    
class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.get_fields()]


class CourseAllotmentAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'faculty_abbreviation', 'staff_abbreviation']


class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentAchievement._meta.get_fields()]

class AdminCredentialsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AdminCredentials._meta.get_fields()]

class SubAdminCredentialsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SubAdminCredentials._meta.get_fields()]

class AcademicYearAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AcademicYear._meta.get_fields()]


class MarksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Marks._meta.get_fields()]

class AttendanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Attendance._meta.get_fields()]



admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(CourseAllotment,CourseAllotmentAdmin)
admin.site.register(StudentAchievement,StudentAchievementAdmin)
admin.site.register(AdminCredentials,AdminCredentialsAdmin)
admin.site.register(SubAdminCredentials,SubAdminCredentialsAdmin)
admin.site.register(AcademicYear,AcademicYearAdmin)
admin.site.register(Marks,MarksAdmin)
admin.site.register(Attendance,AttendanceAdmin)