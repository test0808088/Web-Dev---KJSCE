from django.urls import path, include
from user_handler import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('faculty', views.FacultyViewSet, basename='faculty')
router.register('staff', views.StaffViewSet, basename='staff')
router.register('student', views.StudentViewSet, basename='student')
router.register('course', views.CourseViewSet, basename='course')
router.register('course-assignment', views.CourseAssignmentViewSet, basename='course-assignment')


urlpatterns = [
    path('', include(router.urls)),
    path('download-csv/<str:model>/', views.DownloadCSV.as_view(), name='download-csv'),
    
]