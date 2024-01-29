from django.db import models

class Faculty(models.Model):
    DEPT_CHOICES = (
        ('Comps', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )

    dept = models.CharField(max_length=100, choices=DEPT_CHOICES)
    employee_code = models.PositiveIntegerField(unique=True)
    faculty_abbreviation = models.CharField(max_length=20, primary_key=True,unique=True)
    faculty_name = models.CharField(max_length=100)
    faculty_email = models.EmailField(max_length=100)
    experience = models.PositiveIntegerField(null=True)
    post = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)

class Staff(models.Model):
    DEPT_CHOICES = (
        ('Comps', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )

    dept = models.CharField(max_length=100, choices=DEPT_CHOICES)
    employee_code = models.PositiveIntegerField(unique=True)
    staff_abbreviation = models.CharField(max_length=20, primary_key=True, unique=True)
    staff_name = models.CharField(max_length=100)
    staff_email = models.EmailField(max_length=100)
    experience = models.PositiveIntegerField(null=True)
    post = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)

class Student(models.Model):
    BRANCH_CHOICES = (
        ('Comps', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )
    student_branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    student_name = models.CharField(max_length=100)
    roll_number = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=100)
    proctor_abbreviation = models.ForeignKey(Faculty, on_delete=models.CASCADE, to_field='faculty_abbreviation')
    student_contact_no = models.CharField(max_length=20)
    parents_contact_no = models.CharField(max_length=20)
    parent_email_id = models.EmailField(max_length=100)

class Course(models.Model):
    BRANCH_CHOICES = (
        ('Comps', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    course_code = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=100)
    sem = models.IntegerField()
    scheme_name = models.CharField(max_length=100)
    credit = models.IntegerField()
    hours = models.IntegerField()


class CourseAllotment(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=100)
    faculty_abbreviation = models.CharField(max_length=20, unique=True)
    staff_abbreviation = models.CharField(max_length=20, unique=True)


class StudentAchievement(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements_student_name')
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements_roll_number')
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    upload_file = models.FileField(upload_to='achievements/')

    def __str__(self):
        return f"{self.student_name.student_name} - {self.roll_number.roll_number} - {self.description}"

class AdminCredentials(models.Model):
    admin_username = models.CharField(max_length=20,primary_key=True,unique=True)
    admin_password = models.CharField(max_length=20)

class SubAdminCredentials(models.Model):
    sub_admin_username = models.CharField(max_length=20,primary_key=True,unique=True)
    sub_admin_password = models.CharField(max_length=20)

class AcademicYear(models.Model):
    year = models.CharField(max_length=20, unique=True)
    session = models.CharField(max_length=20)
    