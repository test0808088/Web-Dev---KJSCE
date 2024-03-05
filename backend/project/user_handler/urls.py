from django.urls import path, include
from user_handler import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('faculty', views.FacultyViewSet, basename='faculty')
router.register('staff', views.StaffViewSet, basename='staff')
router.register('student', views.StudentViewSet, basename='student')
router.register('course', views.CourseViewSet, basename='course')
router.register('courseallotment', views.CourseAllotmentViewSet, basename='courseallotment')
router.register('marks', views.MarksViewSet, basename='marks')
router.register('attendance', views.AttendanceViewSet, basename='attendance')
router.register('studentachievement', views.StudentAchievementViewSet, basename='studentachievement')


urlpatterns = [
    path('', include(router.urls)),
    path('marks/<str:course_code>/<int:roll_number>/', views.MarksViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='marks-retrieve-delete'),
    path('attendance/<str:course_code>/<int:roll_number>/', views.AttendanceViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='attendance-retrieve-delete'),
    path('download-csv/<str:model>/', views.DownloadCSV.as_view(), name='download-csv'),
    
]