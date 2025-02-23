from .models import Student, Course
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from .forms import EnrollmentForm
from django.shortcuts import render

# Views
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class EnrollmentView(FormView):
    template_name = 'enroll.html'
    form_class = EnrollmentForm
    success_url = reverse_lazy('confirmation')

    def form_valid(self, form):
        student, created = Student.objects.get_or_create(
            email=form.cleaned_data['email'],
            defaults={'name': form.cleaned_data['name']}
        )
        student.courses.set(form.cleaned_data['courses'])
        return super().form_valid(form)
