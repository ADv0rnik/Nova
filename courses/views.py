import logging
from functools import lru_cache

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Course, Module


logger = logging.getLogger("adukar")
logger.event_source = __name__


class CoursesView(ListView):
    model = Course
    template_name = "courses.html"
    queryset = Course.objects.defer("created_at", "updated_at").prefetch_related
    context_object_name = "courses"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Courses list"
        context["course_num"] = Course.objects.count()
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_view.html"
    context_object_name = "course"
    slug_url_kwarg = "course_slug"

    def get_queryset(self):
        course = Course.objects.filter(slug=self.kwargs["course_slug"])
        return course

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modules"] = context["course"].course_module.all()
        return context


@lru_cache()
def index(request):
    return render(request, "home.html")
