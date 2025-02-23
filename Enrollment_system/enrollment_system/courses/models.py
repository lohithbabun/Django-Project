from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django import forms
from django.shortcuts import render

# Models
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name