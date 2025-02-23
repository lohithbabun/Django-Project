from django.urls import path
from .views import CourseListView, EnrollmentView
from django.shortcuts import render

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('enroll/', EnrollmentView.as_view(), name='enroll'),
    path('confirmation/', lambda request: render(request, 'confirmation.html'), name='confirmation'),
]
