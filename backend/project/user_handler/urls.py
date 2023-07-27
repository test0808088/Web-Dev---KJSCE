from django.urls import path, include
from user_handler import views
from rest_framework.routers import DefaultRouter
from .views import upload_csv

router = DefaultRouter()

router.register('faculty', views.facultyViewSet, basename='fauclty')
router.register('staff', views.staffViewSet, basename='staff')

urlpatterns = [
    path('', include(router.urls)),
    path('download-csv/<str:model>/', views.DownloadCSV.as_view(), name='download-csv'),
    # path('upload-csv/', views.UploadCSV.as_view(), name='upload-csv'),
    path('upload-csv/', upload_csv, name='upload-csv'),
]