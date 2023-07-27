from django.shortcuts import render, HttpResponse
from . import models
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
import csv
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .forms import CSVUploadForm
import os

# Create your views here.

class facultyViewSet(viewsets.ModelViewSet):
    queryset = models.faculty.objects.all()
    serializer_class = serializers.faculty_serializer 

    def put(self, request, id=None):
        faculty = models.faculty.objects.all()
        serializer = serializers.faculty_serializer(faculty, data = request.data)
        return Response(serializer.data)
    

class staffViewSet(viewsets.ModelViewSet):
    queryset = models.staff.objects.all()
    serializer_class = serializers.staff_serializer

    def put(self, request, id=None):
        staff = models.staff.objects.all()
        serializer = serializers.staff_serializer(staff, data = request.data)
        return Response(serializer.data)
    

class DownloadCSV(APIView):
    def get(self, request, model):
        if model == 'faculty':
            queryset = models.faculty.objects.all()
            serializer_class = serializers.faculty_serializer
        elif model == 'staff':
            queryset = models.staff.objects.all()
            serializer_class = serializers.staff_serializer
        else:
            return Response({'message': 'Invalid model name.'}, status=400)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(model)

        serializer = serializer_class(queryset, many=True)

        field_names = ['branch', 'dept', 'employee_code', 'faculty_name', 'employee_abbreviation',
                       'faculty_email', 'experience', 'post'] if model == 'faculty' else ['branch', 'dept', 'employee_code', 'staff_name', 'employee_abbreviation',
                       'staff_email', 'experience', 'post']

        writer = csv.DictWriter(response, fieldnames=field_names)
        writer.writeheader()
        for data in serializer.data:
            writer.writerow(data)

        return response


# class UploadCSV (APIView):

def upload_csv(request):
        if request.method == 'POST':
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']

                # Save the uploaded CSV file to the media folder
                file_path = os.path.join('user_handler', 'media', csv_file.name)
                with open(file_path, 'wb') as destination:
                    for chunk in csv_file.chunks():
                        destination.write(chunk)

                # Read the CSV file and create model instances
                with open(file_path, 'r') as file:
                    csv_data = csv.reader(file)
                    next(csv_data)  # Skip the header row
                    for row in csv_data:
                        branch = row[0]
                        dept = row[1]
                        emplyoee_code = row[2]
                        faculty_name = row[3]
                        employee_abbreviation = row[4]
                        faculty_email = row[5]
                        experience = row[6]
                        post = row[7]

                        # Create a new instance of ShopModels
                        faculty = models.faculty(branch=branch, dept=dept, employee_code=emplyoee_code,
                                                faculty_name=faculty_name, employee_abbreviation=employee_abbreviation, faculty_email=faculty_email, experience=experience, post=post)
                        faculty.save()

                # Optionally, you can show a success message or redirect to a different page
                return HttpResponse("Data successfully added into models")
        else:
            form = CSVUploadForm()

        return render(request, 'upload_csv.html', {'form': form})

# class csvdownloadViewSet(viewsets.ModelViewSet):

