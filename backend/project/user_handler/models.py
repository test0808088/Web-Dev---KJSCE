from django.db import models

class branch(models.Model):
    # branch_choices = [
    #     ('Comps', 'Computer Science'),
    #     ('IT', 'Information Technology'),
    #     ('EXTC', 'Electronics and Telecommunication'),
    #     ('ETRX', 'Electronics'),
    #     ('MECH', 'Mechanical'),
    # ]
    
    branch_name = models.CharField(max_length=50, unique=True, primary_key=True)
    def __str__(self):
        return str(self.branch_name)
    


class faculty(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    dept=models.CharField(max_length=100)
    employee_code = models.PositiveIntegerField()
    faculty_name = models.CharField(max_length=100)
    employee_abbreviation = models.CharField(max_length=20,primary_key=True)
    faculty_email = models.EmailField(max_length=100)
    experience=models.PositiveIntegerField(null = True)
    post=models.CharField(max_length=100)

class staff(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    dept=models.CharField(max_length=100)
    employee_code = models.PositiveIntegerField()
    staff_name = models.CharField(max_length=100)
    employee_abbreviation = models.CharField(max_length=20,primary_key=True)
    staff_email = models.EmailField(max_length=100)
    experience=models.PositiveIntegerField(null = True)
    post=models.CharField(max_length=100)

class Student(models.Model):
    student_branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    Roll_number=models.PositiveBigIntegerField()
    email=models.EmailField(max_length=100)
    Proctor_Abbreviation = models.ForeignKey(faculty,on_delete=models.CASCADE,to_field='employee_abbreviation')
    Student_contact_no=models.CharField(max_length=20)
    Parents_contact_no=models.CharField(max_length=20)
    Parent_email_id=models.EmailField(max_length=100)

class Course(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20,primary_key=True)
    course_name = models.CharField(max_length=100)
    Dept=models.CharField(max_length=100)
    Sem=models.IntegerField()
    Scheme_name=models.CharField(max_length=100)
    Credit=models.IntegerField()
    Hours=models.IntegerField()




# Register your models here.


# Create your models here.
