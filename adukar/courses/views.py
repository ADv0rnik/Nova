from django.shortcuts import render
from django.views.generic import ListView

from .models import Course


class CoursesView(ListView):
    model = Course
    template_name = 'courses.html'
    queryset = Course.objects.all()
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Courses list'
        return context


