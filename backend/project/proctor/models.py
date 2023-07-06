from django.db import models
from admin import models
from admin.models import Student,Staff


# Create your models here.


class Proctor(models.Model):
    employee_code = models.ForeignKey(Staff, Student, on_delete=models.CASCADE)
    
        
    # dept = models.CharField(max_length=15, blank=False, null=False)
    # employee_code = models.IntegerField(max_length=25, blank=False, null=False)
    # faculty_name = models.CharField(max_length=100, blank=False, null=False)
    # employee_abr = models.CharField(primary_key=True, max_length=3, blank=False, null=False)
    # faculty_email = models.EmailField(max_length=100, blank=False, null=False)
    # experience = models.IntegerField(max_length=15, blank=False, null=False)
    # post = models.CharField(max_length=15, blank=False, null=False)

class registered_students:
    Proctor_abr = models.ForeignKey(Proctor, on_delete=models.CASCADE)
    Roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, blank=False, null=False)
    Dept = models.CharField(max_length=15, blank=False, null=False)
    
    