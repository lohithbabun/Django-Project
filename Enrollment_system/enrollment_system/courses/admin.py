from django.contrib import admin

# Admin (in admin.py)
from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    filter_horizontal = ('courses',)  # For better Many-to-Many UI