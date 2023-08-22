
# modified code



from django.db import models


class Faculty(models.Model):
    BRANCH_CHOICES = (
        ('Comps', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    dept = models.CharField(max_length=100, default='null')
    employee_code = models.PositiveIntegerField()
    faculty_name = models.CharField(max_length=100)
    employee_abbreviation = models.CharField(max_length=20, primary_key=True)
    faculty_email = models.EmailField(max_length=100)
    experience = models.PositiveIntegerField(null=True)
    post = models.CharField(max_length=100)
    
    def __str__(self):
        return self.faculty_name


class Staff(models.Model):
    BRANCH_CHOICES = (
        ('Comps', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EXTC', 'Electronics and Telecommunication'),
        ('ETRX', 'Electronics'),
        ('MECH', 'Mechanical'),
    )
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    dept = models.CharField(max_length=100)
    employee_code = models.PositiveIntegerField()
    staff_name = models.CharField(max_length=100)
    employee_abbreviation = models.CharField(max_length=20, primary_key=True)
    staff_email = models.EmailField(max_length=100)
    experience = models.PositiveIntegerField(null=True)
    post = models.CharField(max_length=100)


# class Proctor(models.Model):
#     faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE, primary_key=True, default=Faculty.objects.get, limit_choices_to={'employee_abbreviation': 'DEFAULT_PROCTOR_FACULTY'})

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
    proctor = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
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
    dept = models.CharField(max_length=100)
    sem = models.IntegerField()
    scheme_name = models.CharField(max_length=100)
    credit = models.IntegerField()
    hours = models.IntegerField()


class CourseAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    # assignment_date = models.DateTimeField(auto_now_add=True)