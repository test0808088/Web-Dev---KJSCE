from faker import Faker
from user_handler.models import *
import random
import string

fake = Faker()



def seed_faculty():
    for i in range(10):
        branch = Branch.objects.get(branch_name='Comps')
        dept = fake.job()
        employee_code = fake.pyint()
        faculty_name = fake.name()
        employee_abbreviation = ''.join(random.choices(string.ascii_uppercase, k=3))
        faculty_email = fake.email()
        experience = fake.pyint()
        post = fake.job()
        faculty.objects.create(branch=branch, dept=dept, employee_code=employee_code, faculty_name=faculty_name, employee_abbreviation=employee_abbreviation, faculty_email=faculty_email, experience=experience, post=post)
    for i in range(10):
        branch = Branch.objects.get(branch_name='IT')
        dept = fake.job()
        employee_code = fake.pyint()
        faculty_name = fake.name()
        employee_abbreviation = ''.join(random.choices(string.ascii_uppercase, k=3))
        faculty_email = fake.email()
        experience = fake.pyint()
        post = fake.job()
        faculty.objects.create(branch=branch, dept=dept, employee_code=employee_code, faculty_name=faculty_name, employee_abbreviation=employee_abbreviation, faculty_email=faculty_email, experience=experience, post=post)

def seed_staff():
    for i in range(10):
        branch = Branch.objects.get(branch_name='Comps')
        dept = fake.job()
        employee_code = fake.pyint()
        staff_name = fake.name()
        employee_abbreviation = ''.join(random.choices(string.ascii_uppercase, k=3))
        staff_email = fake.email()
        experience = fake.pyint()
        post = fake.job()
        staff.objects.create(branch=branch, dept=dept, employee_code=employee_code, staff_name=staff_name, employee_abbreviation=employee_abbreviation, staff_email=staff_email, experience=experience, post=post)

def seed_student(n):
    for i in range(n):
        branch = Branch.objects.get(branch_name='Comps')
        student_name = fake.name()
        Roll_number = fake.pyint()
        email = fake.email()
        Proctor_Abbreviation = faculty.objects.get(employee_abbreviation='UJP')
        Student_contact_no = fake.pyint()
        Parents_contact_no = fake.pyint()
        Parent_email_id = fake.email()
        Student.objects.create(student_branch=branch, student_name=student_name, Roll_number=Roll_number, email=email, Proctor_Abbreviation=Proctor_Abbreviation, Student_contact_no=Student_contact_no, Parents_contact_no=Parents_contact_no, Parent_email_id=Parent_email_id)
    
    for i in range(n):
        branch = Branch.objects.get(branch_name='IT')
        student_name = fake.name()
        Roll_number = fake.pyint()
        email = fake.email()
        Proctor_Abbreviation = faculty.objects.get(employee_abbreviation='UJP')
        Student_contact_no = fake.pyint()
        Parents_contact_no = fake.pyint()
        Parent_email_id = fake.email()
        Student.objects.create(student_branch=branch, student_name=student_name, Roll_number=Roll_number, email=email, Proctor_Abbreviation=Proctor_Abbreviation, Student_contact_no=Student_contact_no, Parents_contact_no=Parents_contact_no, Parent_email_id=Parent_email_id)
    
    for i in range(n):
        branch = Branch.objects.get(branch_name='ETRX')
        student_name = fake.name()
        Roll_number = fake.pyint()
        email = fake.email()
        Proctor_Abbreviation = faculty.objects.get(employee_abbreviation='UJP')
        Student_contact_no = fake.pyint()
        Parents_contact_no = fake.pyint()
        Parent_email_id = fake.email()
        Student.objects.create(student_branch=branch, student_name=student_name, Roll_number=Roll_number, email=email, Proctor_Abbreviation=Proctor_Abbreviation, Student_contact_no=Student_contact_no, Parents_contact_no=Parents_contact_no, Parent_email_id=Parent_email_id)
