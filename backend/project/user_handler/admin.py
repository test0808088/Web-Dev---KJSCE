from django.contrib import admin

from .models import Faculty, Staff, Student, Course,CourseAllotment,StudentAchievement,AdminCredentials, SubAdminCredentials, AcademicYear

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
        'parent_email_id', 'display_proctor_info'
    ]

    def display_proctor_info(self, obj):
        return f"{obj.proctor_abbreviation.dept} - {obj.proctor_abbreviation.faculty_name}"

    display_proctor_info.short_description = 'Proctor Information'

    

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



admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(CourseAllotment,CourseAllotmentAdmin)
admin.site.register(StudentAchievement,StudentAchievementAdmin)
admin.site.register(AdminCredentials,AdminCredentialsAdmin)
admin.site.register(SubAdminCredentials,SubAdminCredentialsAdmin)
admin.site.register(AcademicYear,AcademicYearAdmin)