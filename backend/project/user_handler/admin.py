from django.contrib import admin

# Register your models here.

from .models import Branch, faculty, staff, Student, Course, Year

admin.site.register(Branch)
admin.site.register(faculty)
admin.site.register(staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Year)