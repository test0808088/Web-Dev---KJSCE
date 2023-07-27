from django.contrib import admin

# Register your models here.

from .models import branch, faculty, staff, Student, Course

admin.site.register(branch)
admin.site.register(faculty)
admin.site.register(staff)
admin.site.register(Student)
admin.site.register(Course)
