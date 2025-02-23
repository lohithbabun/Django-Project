from .models import Student, Course
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django import forms
from django.shortcuts import render

# Forms
class EnrollmentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = ['name', 'email', 'courses']