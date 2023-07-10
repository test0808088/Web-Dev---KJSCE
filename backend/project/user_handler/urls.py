from django.urls import path, include
from user_handler import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('faculty', views.facultyViewSet, basename='fauclty')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.facultyViewSet.as_view()),
]