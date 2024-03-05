
from io import TextIOWrapper
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import csv
from . import serializers
from . import models
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage

class FacultyViewSet(viewsets.ViewSet):
    def list(self, request):
        faculties = models.Faculty.objects.all()
        serializer = serializers.FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            faculty_instance = models.Faculty.objects.get(pk=pk)
            serializer = serializers.FacultySerializer(faculty_instance)
            return Response(serializer.data)
        except models.Faculty.DoesNotExist:
            return Response({"message": "Faculty not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
           
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            next(csv_data, None)

            for row in csv_data:
                
                dept = row[0]
                employee_code = int(row[1])
                faculty_abbreviation = row[2]
                faculty_name = row[3]
                faculty_email = row[4]
                experience = int(row[5])
                post = row[6]
                mobile_number = row[7]
                
                try:
                    faculty_instance = models.Faculty.objects.get(faculty_abbreviation=faculty_abbreviation)
                except models.Faculty.DoesNotExist:
                    faculty_instance = None

                if faculty_instance:
                    
                    serializer = serializers.FacultySerializer(faculty_instance, data={
                        
                        'dept' : dept,
                        'employee_code' : employee_code,
                        'faculty_name' : faculty_name,
                        'faculty_email' : faculty_email,
                        'experience' : experience,
                        'post' : post,
                        'mobile_number' : mobile_number,
   
                        
                    }, partial=True)
                else:
                    
                    serializer = serializers.FacultySerializer(data={
                        
                        'dept' : dept,
                        'employee_code' : employee_code,
                        'faculty_abbreviation' : faculty_abbreviation,
                        'faculty_name' : faculty_name,
                        'faculty_email' : faculty_email,
                        'experience' : experience,
                        'post' : post,
                        'mobile_number' : mobile_number,
                          
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to faculty models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            faculty_instance = models.Faculty.objects.get(pk=pk)
            faculty_instance.delete()
            return Response({"message": "Faculty deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Faculty.DoesNotExist:
            return Response({"message": "Faculty not found."}, status=status.HTTP_404_NOT_FOUND)

class StaffViewSet(viewsets.ViewSet):
    def list(self, request):
        staffs = models.Staff.objects.all()
        serializer = serializers.StaffSerializer(staffs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            staff_instance = models.Staff.objects.get(pk=pk)
            serializer = serializers.StaffSerializer(staff_instance)
            return Response(serializer.data)
        except models.Staff.DoesNotExist:
            return Response({"message": "Staff not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:

                dept = row[0]
                employee_code = int(row[1])
                staff_abbreviation = row[2]
                staff_name = row[3]
                staff_email = row[4]
                experience = int(row[5])
                post = row[6]
                mobile_number = row[7]

                try:
                    staff_instance = models.Staff.objects.get(staff_abbreviation=staff_abbreviation)
                except models.Staff.DoesNotExist:
                    staff_instance = None

                if staff_instance:
                    
                    serializer = serializers.StaffSerializer(staff_instance, data={
                        
                        'dept' : dept,
                        'employee_code' : employee_code,
                        'staff_name' : faculty_name,
                        'staff_email' : faculty_email,
                        'experience' : experience,
                        'post' : post,
                        'mobile_number' : mobile_number,
                           
                    }, partial=True)
                else:
                    
                    serializer = serializers.StaffSerializer(data={
                        
                        'dept' : dept,
                        'employee_code' : employee_code,
                        'staff_abbreviation' : staff_abbreviation,
                        'staff_name' : staff_name,
                        'staff_email' : staff_email,
                        'experience' : experience,
                        'post' : post,
                        'mobile_number' : mobile_number,
    
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to staff models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            staff_instance = models.Staff.objects.get(pk=pk)
            staff_instance.delete()
            return Response({"message": "Staff deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Staff.DoesNotExist:
            return Response({"message": "Staff not found."}, status=status.HTTP_404_NOT_FOUND)

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = models.Student.objects.all()
        serializer = serializers.StudentSerializer(students, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            student_instance = models.Student.objects.get(pk=pk)
            serializer = serializers.StudentSerializer(student_instance)
            return Response(serializer.data)
        except models.Student.DoesNotExist:
            return Response({"message": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:

                student_branch = row[0]
                student_name = row[1]
                roll_number = int(row[2])
                email = row[3]
                proctor_abbreviation = row[4]
                student_contact_no = row[5]
                parents_contact_no = row[6]
                parent_email_id = row[7]
                year = row[8]
                session = row[9]
                course_1 = row[10]
                course_2 = row[11]
                course_3 = row[12]
                course_4 = row[13]
                course_5 = row[14]
                course_6 = row[15]
                course_7 = row[16]
                course_8 = row[17]
                course_9 = row[18]
                course_10 = row[19]
                course_11 = row[20]
                course_12 = row[21]
                course_13 = row[22]
                course_14 = row[23]
                course_15 = row[24]

                
                try:
                    student_instance = models.Student.objects.get(roll_number=roll_number)
                except models.Student.DoesNotExist:
                    student_instance = None

                if student_instance:
                    
                    serializer = serializers.StudentPostSerializer(student_instance, data={
                        'student_branch' : student_branch,
                        'student_name' : student_name,
                        'roll_number' : roll_number,
                        'email' : email,
                        'proctor_abbreviation' : proctor_abbreviation,
                        'student_contact_no' : student_contact_no,
                        'parents_contact_no' : parents_contact_no,
                        'parent_email_id' : parent_email_id,
                        'year' : year,
                        'session' : session,
                        'course_1' : course_1,
                        'course_2' : course_2,
                        'course_3' : course_3,
                        'course_4' : course_4,
                        'course_5' : course_5,
                        'course_6' : course_6,
                        'course_7' : course_7,
                        'course_8' : course_8,
                        'course_9' : course_9,
                        'course_10' : course_10,
                        'course_11' : course_11,
                        'course_12' : course_12,
                        'course_13' : course_13,
                        'course_14' : course_14,
                        'course_15' : course_15,

                        
                    }, partial=True)
                else:
                    
                    serializer = serializers.StudentPostSerializer(data={
                        'student_branch' : student_branch,
                        'student_name' : student_name,
                        'roll_number' : roll_number,
                        'email' : email,
                        'proctor_abbreviation' : proctor_abbreviation,
                        'student_contact_no' : student_contact_no,
                        'parents_contact_no' : parents_contact_no,
                        'parent_email_id' : parent_email_id,
                        'year' : year,
                        'session' : session,
                        'course_1' : course_1,
                        'course_2' : course_2,
                        'course_3' : course_3,
                        'course_4' : course_4,
                        'course_5' : course_5,
                        'course_6' : course_6,
                        'course_7' : course_7,
                        'course_8' : course_8,
                        'course_9' : course_9,
                        'course_10' : course_10,
                        'course_11' : course_11,
                        'course_12' : course_12,
                        'course_13' : course_13,
                        'course_14' : course_14,
                        'course_15' : course_15,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Student models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            student_instance = models.Student.objects.get(pk=pk)
            student_instance.delete()
            return Response({"message": "Student deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Student.DoesNotExist:
            return Response({"message": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            course_instance = models.Course.objects.get(pk=pk)
            serializer = serializers.CourseSerializer(course_instance)
            return Response(serializer.data)
        except models.Course.DoesNotExist:
            return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:
                
                branch = row[0]
                course_code = row[1]
                course_name = row[2]
                sem = row[3]
                scheme_name = row[4]
                credit = row[5]
                hours = row[6]
                
                try:
                    course_instance = models.Course.objects.get(course_code=course_code)
                except models.Course.DoesNotExist:
                    course_instance = None

                if course_instance:
                    
                    serializer = serializers.CourseSerializer(course_instance, data={
                        
                        'branch' : branch,
                        'course_name' : course_name,
                        'sem' : sem,
                        'scheme_name' : scheme_name,
                        'credit' : credit,
                        'hours' : hours,

                    }, partial=True)
                else:
                    
                    serializer = serializers.CourseSerializer(data={
                        
                        'branch' : branch,
                        'course_code' : course_code,
                        'course_name' : course_name,
                        'sem' : sem,
                        'scheme_name' : scheme_name,
                        'credit' : credit,
                        'hours' : hours,
 
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Course models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            course_instance = models.Course.objects.get(pk=pk)
            course_instance.delete()
            return Response({"message": "Course deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Course.DoesNotExist:
            return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)


class CourseAllotmentViewSet(viewsets.ViewSet):
    def list(self, request):
        courses_allotments = models.CourseAllotment.objects.all()
        serializer = serializers.CourseAllotmentSerializer(courses_allotments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            course_allotment_instance = models.CourseAllotment.objects.get(pk=pk)
            serializer = serializers.CourseAllotmentSerializer(course_allotment_instance)
            return Response(serializer.data)
        except models.CourseAllotment.DoesNotExist:
            return Response({"message": "Course Allotment not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
           
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            next(csv_data, None)

            for row in csv_data:

                course_code= row[0]
                course_name= row[1]
                faculty_abbreviation= row[2]
                staff_abbreviation= row[3]
                
                try:
                    course_allotment_instance = models.CourseAllotment.objects.get(course_code=course_code)
                except models.CourseAllotment.DoesNotExist:
                    course_allotment_instance = None

                if course_allotment_instance:
                    
                    serializer = serializers.CourseAllotmentSerializer(course_allotment_instance, data={
                        
                        'course_name': course_name,
                        'faculty_abbreviation': faculty_abbreviation,
                        'staff_abbreviation': staff_abbreviation,
   
                    }, partial=True)
                else:
                    serializer = serializers.CourseAllotmentSerializer(data={
                        
                        'course_code': course_code,
                        'course_name': course_name,
                        'faculty_abbreviation': faculty_abbreviation,
                        'staff_abbreviation': staff_abbreviation,
                           
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Course Allotment models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            course_allotment_instance = models.CourseAllotment.objects.get(pk=pk)
            course_allotment_instance.delete()
            return Response({"message": "Course  Allotment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.CourseAllotment.DoesNotExist:
            return Response({"message": "Course Allotment not found."}, status=status.HTTP_404_NOT_FOUND)


class MarksViewSet(viewsets.ViewSet):
    def list(self, request):
        marks = models.Marks.objects.all()
        serializer = serializers.MarksSerializer(marks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, course_code=None, roll_number=None):
        try:
            mark_instance = models.Marks.objects.get(course_code=course_code, roll_number=roll_number)
            serializer = serializers.MarksSerializer(mark_instance)
            return Response(serializer.data)
        except models.Marks.DoesNotExist:
            return Response({"message": "Marks record not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:

                year = row[0]
                session = row[1]
                branch = row[2]
                course_code = row[3]
                course_name = row[4]
                student_name =row[5]
                roll_number = row[6]
                ise = row[7]
                ia1 = row[8]
                ia2 = row[9]
                ia3 = row[10]
                ca = row[11]
                ese = row[12]
                tw = row[13]
                oral=row[14]

                try:
                    mark_instance = models.Marks.objects.get(course_code=course_code,roll_number=roll_number)
                except models.Marks.DoesNotExist:
                    mark_instance = None

                if mark_instance:
                    
                    serializer = serializers.MarksSerializer(mark_instance, data={
                        
                        'year': year,
                        'session': session,
                        'branch': branch, 
                        'course_name': course_name,
                        'student_name': student_name,
                        'ise': ise, 
                        'ia1': ia1, 
                        'ia2': ia2,
                        'ia3': ia3, 
                        'ca': ca,
                        'ese': ese,
                        'tw': tw, 
                        'oral': oral,

                           
                    }, partial=True)
                else:
                    
                    serializer = serializers.MarksSerializer(data={

                        'year': year,
                        'session': session,
                        'branch': branch, 
                        'course_code': course_code,
                        'course_name': course_name,
                        'student_name': student_name,
                        'roll_number': roll_number,
                        'ise': ise, 
                        'ia1': ia1, 
                        'ia2': ia2,
                        'ia3': ia3, 
                        'ca': ca,
                        'ese': ese,
                        'tw': tw, 
                        'oral': oral,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Marks models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, course_code=None, roll_number=None):
        try:
            mark_instance = models.Marks.objects.get(course_code=course_code, roll_number=roll_number)
            mark_instance.delete()
            return Response({"message": "Marks data deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Marks.DoesNotExist:
            return Response({"message": "Marks data not found."}, status=status.HTTP_404_NOT_FOUND)


class AttendanceViewSet(viewsets.ViewSet):
    def list(self, request):
        attendance = models.Attendance.objects.all()
        serializer = serializers.AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    def retrieve(self, request, course_code=None, roll_number=None):
        try:
            attendance_instance = models.Attendance.objects.get(course_code=course_code, roll_number=roll_number)
            serializer = serializers.AttendanceSerializer(attendance_instance)
            return Response(serializer.data)
        except models.Attendance.DoesNotExist:
            return Response({"message": "Attendance record not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:


                year = row[0]
                session = row[1]
                branch = row[2]
                course_code = row[3]
                course_name = row[4]
                student_name =row[5]
                roll_number = row[6]
                january= row[7]
                february=row[8]
                march=row[9]
                april=row[10]
                may=row[11]
                june=row[12]
                july=row[13]
                august=row[14]
                september=row[15]
                october=row[16]
                november=row[17]
                december=row[18]
                

                try:
                    attendance_instance = models.Attendance.objects.get(course_code=course_code,roll_number=roll_number)
                except models.Attendance.DoesNotExist:
                    attendance_instance = None

                if attendance_instance:
                    
                    serializer = serializers.AttendanceSerializer(attendance_instance, data={
                        
                        'year': year,
                        'session': session,
                        'branch': branch, 
                        'course_name': course_name,
                        'student_name': student_name,
                        'january': january,
                        'february':february,
                        'march':march,
                        'april':april,
                        'may':may,
                        'june':june,
                        'july':july,
                        'august':august,
                        'september':september,
                        'october':october,
                        'november':november,
                        'december':december,

                           
                    }, partial=True)
                else:
                    
                    serializer = serializers.AttendanceSerializer(data={

                        'year': year,
                        'session': session,
                        'branch': branch, 
                        'course_code': course_code,
                        'course_name': course_name,
                        'student_name': student_name,
                        'roll_number': roll_number,
                        'january': january,
                        'february':february,
                        'march':march,
                        'april':april,
                        'may':may,
                        'june':june,
                        'july':july,
                        'august':august,
                        'september':september,
                        'october':october,
                        'november':november,
                        'december':december,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Attendance models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, course_code=None, roll_number=None):
        try:
            attendance_instance = models.Attendance.objects.get(course_code=course_code, roll_number=roll_number)
            attendance_instance.delete()
            return Response({"message": "Attendance data deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Attendance.DoesNotExist:
            return Response({"message": "Attendance data not found."}, status=status.HTTP_404_NOT_FOUND)


class DownloadCSV(APIView):

    allowed_methods = ['GET', 'POST']

    def get(self, request, model):
        if model == 'Faculty':
            queryset = models.Faculty.objects.none()  
            serializer_class = serializers.FacultySerializer
        elif model == 'Staff':
            queryset = models.Staff.objects.none()  
            serializer_class = serializers.StaffSerializer
        elif model == 'Student':
            queryset = models.Student.objects.none()  
            serializer_class = serializers.StudentSerializer
        elif model == 'Course':
            queryset = models.Course.objects.none()  
            serializer_class = serializers.CourseSerializer
        elif model == 'CourseAllotment':
            queryset = models.CourseAllotment.objects.none()
            serializer_class = serializers.CourseAllotmentSerializer
        elif model == 'Marks':
            queryset = models.Marks.objects.none()
            serializer_class = serializers.MarksSerializer
        elif model == 'Attendance':
            queryset = models.Attendance.objects.none()
            serializer_class = serializers.AttendanceSerializer
        else:
            return Response({'message': 'Invalid model name.'}, status=400)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(model)

        serializer = serializer_class(queryset, many=True)

        field_names = ['dept', 'employee_code', 'faculty_abbreviation', 'faculty_name',
                       'faculty_email', 'experience', 'post', 'mobile_number'] if model == 'Faculty' else ['dept', 'employee_code', 'staff_abbreviation', 'staff_name',
                       'staff_email', 'experience', 'post', 'mobile_number'] if model == 'Staff' else ['student_branch', 'student_name', 'roll_number', 'email', 'proctor_abbreviation',
                       'student_contact_no', 'parents_contact_no', 'parent_email_id', 'year', 'session', 'course_1','course_2', 'course_3', 'course_4', 'course_5', 'course_6', 'course_7', 'course_8', 'course_9', 'course_10', 'course_11', 'course_12', 'course_13', 'course_14', 'course_15'] if model == 'Student' else ['branch', 'course_code', 'course_name', 'sem',
                       'scheme_name', 'credit', 'hours'] if model == 'Course' else ['course_code', 'course_name', 'faculty_abbreviation', 'staff_abbreviation'] if model == 'CourseAllotment' else ['year', 'session', 'branch', 'course_code', 'course_name', 'student_name', 'roll_number', 'ise', 'ia1', 'ia2', 'ia3', 'ca', 'ese', 'tw', 'oral'] if model == 'Marks' else ['year', 'session', 'branch', 'course_code', 'course_name', 'student_name', 'roll_number', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] if model == 'Attendance' else []

        writer = csv.DictWriter(response, fieldnames=field_names)
        writer.writeheader()

        return response


class StudentAchievementViewSet(viewsets.ModelViewSet):

    
    def list(self, request):
        achievements = models.StudentAchievement.objects.all()
        serializer = serializers.StudentAchievementSerializer(achievements, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            achievement_instance = models.StudentAchievement.objects.get(pk=pk)
            serializer = serializers.StudentAchievementSerializer(achievement_instance)
            return Response(serializer.data)
        except models.StudentAchievement.DoesNotExist:
            return Response({"message": "Student Achievement data not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = serializers.StudentAchievementSerializer(data=request.data)
        if serializer.is_valid():
            
            upload_file = request.FILES.get('upload_file')
            fs = FileSystemStorage()
            filename = fs.save(upload_file.name, upload_file)
            serializer.validated_data['upload_file'] = filename
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            achievement_instance = models.StudentAchievement.objects.get(pk=pk)
            achievement_instance.delete()
            return Response({"message": "Student Achievement data deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.StudentAchievement.DoesNotExist:
            return Response({"message": "Student Achievement data not found."}, status=status.HTTP_404_NOT_FOUND)

