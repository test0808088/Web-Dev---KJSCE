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

class Student(models.Model):
    student_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    Roll_number=models.PositiveBigIntegerField()
    email=models.EmailField(max_length=100)
    Proctor_Abbreviation = models.ForeignKey(Faculty,on_delete=models.CASCADE,to_field='Employee_Abbreviation')
    Student_contact_no=models.CharField(max_length=20)
    Parents_contact_no=models.CharField(max_length=20)
    Parent_email_id=models.EmailField(max_length=100)

class Course(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=100)
    Dept=models.CharField(max_length=100)
    Sem=models.IntegerField()
    Scheme_name=models.CharField(max_length=100)
    Credit=models.IntegerField()
    Hours=models.IntegerField()

class Year(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    Year= models.CharField(max_length=4)
    Faculty_name=models.ForeignKey(Faculty, on_delete=models.CASCADE,to_field='Employee_Abbreviation')
    Staff_name=models.ForeignKey(Staff,on_delete=models.CASCADE,to_field='Employee_Abbreviation')
    Course_code=models.ForeignKey(Course,on_delete=models.CASCADE,to_field='course_code')


# Register your models here.


# Create your models here.
