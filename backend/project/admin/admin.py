from django.db import models

class Branch(models.Model):
    branch_choices = [
        ('comps', 'Computer Science'),
        ('it', 'Information Technology'),
        ('extc', 'Electronics and Telecommunication'),
        ('etrx', 'Electronics'),
        ('mech', 'Mechanical'),
    ]
    
    branch_name = models.CharField(max_length=50, choices=branch_choices, unique=True)
    
  

class Faculty(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    Dept=models.CharField(max_length=100)
    Employee_code = models.CharField(max_length=100)
    Faculty_name = models.CharField(max_length=100)
    Employee_Abbreviation = models.CharField(max_length=20,primary_key=True)
    Faculty_email = models.EmailField(max_length=100)
    Experience=models.PositiveIntegerField()
    Post=models.CharField(max_length=100)

class Staff(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    Dept=models.CharField(max_length=100)
    Employee_code = models.CharField(max_length=100)
    staff_name = models.CharField(max_length=100)
    Employee_Abbreviation = models.CharField(max_length=20,primary_key=True)
    Staff_email = models.EmailField(max_length=100)
    Experience=models.PositiveIntegerField()
    Post=models.CharField(max_length=100)

class Students(models.Model):
    student_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    Roll_number=models.PositiveBigIntegerField()
    email=models.EmailField(max_length=100)
    Proctor_Abbreviation = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    Student_contact_no=models.CharField(max_length=20)
    Parents_contact_no=models.CharField(max_length=20)
    Parent_email_id=models.EmailField(max_length=100)

class Course(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    Dept=models.CharField(max_length=100)
    Sem=models.IntegerField(max_length=20)
    Scheme_name=models.CharField(max_length=100)
    Credit=models.IntegerField(max_length=20)
    Hours=models.IntegerField(max_length=20)

class Year(models.Model):


# Register your models here.
