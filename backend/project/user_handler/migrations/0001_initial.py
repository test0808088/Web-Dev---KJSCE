# Generated by Django 4.2.2 on 2023-08-22 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('branch', models.CharField(choices=[('Comps', 'Computer Science'), ('IT', 'Information Technology'), ('EXTC', 'Electronics and Telecommunication'), ('ETRX', 'Electronics'), ('MECH', 'Mechanical')], max_length=20)),
                ('course_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('scheme_name', models.CharField(max_length=100)),
                ('credit', models.IntegerField()),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('branch', models.CharField(choices=[('Comps', 'Computer Science'), ('IT', 'Information Technology'), ('EXTC', 'Electronics and Telecommunication'), ('ETRX', 'Electronics'), ('MECH', 'Mechanical')], max_length=20)),
                ('dept', models.CharField(default='null', max_length=100)),
                ('employee_code', models.PositiveIntegerField()),
                ('faculty_name', models.CharField(max_length=100)),
                ('employee_abbreviation', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('faculty_email', models.EmailField(max_length=100)),
                ('experience', models.PositiveIntegerField(null=True)),
                ('post', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('branch', models.CharField(choices=[('Comps', 'Computer Science'), ('IT', 'Information Technology'), ('EXTC', 'Electronics and Telecommunication'), ('ETRX', 'Electronics'), ('MECH', 'Mechanical')], max_length=20)),
                ('dept', models.CharField(max_length=100)),
                ('employee_code', models.PositiveIntegerField()),
                ('staff_name', models.CharField(max_length=100)),
                ('employee_abbreviation', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('staff_email', models.EmailField(max_length=100)),
                ('experience', models.PositiveIntegerField(null=True)),
                ('post', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_branch', models.CharField(choices=[('Comps', 'Computer Science'), ('IT', 'Information Technology'), ('EXTC', 'Electronics and Telecommunication'), ('ETRX', 'Electronics'), ('MECH', 'Mechanical')], max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('roll_number', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('student_contact_no', models.CharField(max_length=20)),
                ('parents_contact_no', models.CharField(max_length=20)),
                ('parent_email_id', models.EmailField(max_length=100)),
                ('proctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_handler.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='CourseAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_handler.faculty')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.student')),
            ],
        ),
    ]
