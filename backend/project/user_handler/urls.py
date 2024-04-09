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
    
    
    path('marks/<str:exam>/<str:course_code>/<int:roll_number>/delete/', views.MarksViewSet.as_view({'delete': 'delete_exam_marks'}), name='marks-delete-exam'),
    
    path('attendance/<str:month>/<str:course_code>/<int:roll_number>/delete/', views.AttendanceViewSet.as_view({'delete': 'delete_month_attendance'}), name='attendance-delete-month'),

    path('marks/<str:exam>/<str:course_code>/download-csv/', views.DownloadExamCSV.as_view(), name='download-exam-csv'),
    path('marks/<str:course_code>/download-csv/', views.DownloadAllExamCSV.as_view(), name='download-all-exam-csv'),

    path('attendance/<str:month>/<str:course_code>/download-csv/', views.DownloadMonthAttendanceCSV.as_view(), name='download-month-attendance-csv'),
    path('attendance/<str:course_code>/download-csv/', views.DownloadAllMonthAttendanceCSV.as_view(), name='download-all-month-attendance-csv'),

    path('marks/<str:course_code>/<int:roll_number>/', views.MarksViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='marks-retrieve-delete'),
    path('attendance/<str:course_code>/<int:roll_number>/', views.AttendanceViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='attendance-retrieve-delete'),

    path('student/proctor/<str:abbreviation>/', views.StudentByProctorAbbreviation.as_view(), name='student-by-proctor-abbreviation'),

    path('download-csv/<str:model>/', views.DownloadCSV.as_view(), name='download-csv'),
      
    
]