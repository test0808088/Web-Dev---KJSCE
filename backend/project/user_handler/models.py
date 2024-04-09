from django.db import models

class Faculty(models.Model):
    DEPT_CHOICES = (
        ('COMPS', 'Computer Science'),
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
        ('COMPS', 'Computer Science'),
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
        ('COMPS', 'Computer Science'),
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
    year = models.CharField(max_length=20)
    session = models.CharField(max_length=20)
    course_1 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_2 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_3 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_4 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_5 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_6 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_7 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_8 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_9 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_10 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_11 = models.CharField(max_length=100, default='null',blank=True, null=True)
    course_12 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_13 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_14 = models.CharField(max_length=100, default='null', blank=True, null=True)
    course_15 = models.CharField(max_length=100, default='null', blank=True, null=True)

class Course(models.Model):
    BRANCH_CHOICES = (
        ('COMPS', 'Computer Science'),
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
    student_name = models.CharField(max_length=100)
    roll_number = models.PositiveBigIntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    upload_file = models.FileField(upload_to='media/')
    drive_link = models.CharField(max_length=200)


class AdminCredentials(models.Model):
    admin_username = models.CharField(max_length=20,primary_key=True,unique=True)
    admin_password = models.CharField(max_length=20)

class SubAdminCredentials(models.Model):
    sub_admin_username = models.CharField(max_length=20,primary_key=True,unique=True)
    sub_admin_password = models.CharField(max_length=20)

class AcademicYear(models.Model):
    year = models.CharField(max_length=20)
    session = models.CharField(max_length=20)
    

class Marks(models.Model):
    BRANCH_CHOICES = (
        ('COMPS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )

    year = models.CharField(max_length=20)
    session = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    roll_number = models.PositiveBigIntegerField()
    ise = models.PositiveBigIntegerField(blank=True, null=True)
    ia1 = models.PositiveBigIntegerField(blank=True, null=True)
    ia2 = models.PositiveBigIntegerField(blank=True, null=True)
    ia3 = models.PositiveBigIntegerField(blank=True, null=True)
    ca = models.PositiveBigIntegerField(blank=True, null=True)
    ese = models.PositiveBigIntegerField(blank=True, null=True)
    tw = models.PositiveBigIntegerField(blank=True, null=True)
    oral=models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course_code', 'roll_number'], name='unique_marks_course_roll')
        ]


class Attendance(models.Model):
    BRANCH_CHOICES = (
        ('COMPS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )
    
    year = models.CharField(max_length=20)
    session = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    roll_number = models.PositiveBigIntegerField()
    january=models.PositiveBigIntegerField(blank=True, null=True)
    february=models.PositiveBigIntegerField(blank=True, null=True)
    march=models.PositiveBigIntegerField(blank=True, null=True)
    april=models.PositiveBigIntegerField(blank=True, null=True)
    may=models.PositiveBigIntegerField(blank=True, null=True)
    june=models.PositiveBigIntegerField(blank=True, null=True)
    july=models.PositiveBigIntegerField(blank=True, null=True)
    august=models.PositiveBigIntegerField(blank=True, null=True)
    september=models.PositiveBigIntegerField(blank=True, null=True)
    october=models.PositiveBigIntegerField(blank=True, null=True)
    november=models.PositiveBigIntegerField(blank=True, null=True)
    december=models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course_code', 'roll_number'], name='unique_attendance_course_roll')
        ]
    

    