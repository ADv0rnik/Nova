import logging
from functools import lru_cache

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Course, Module
from profiles.models import Profile, CourseResults

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


def get_module_list(request, course_slug):
    # breakpoint()
    # user_id = request.user.id
    # profile = Profile.objects.get(user__id=user_id)
    course = Course.objects.get(slug=course_slug)
    # course_results = CourseResults(
    #     profile=profile,
    #     course=course,
    #     passed=False
    # )
    # course_results.save()

    modules = course.course_module.all()

    context = {
        "course": course,
        "modules": modules,
    }
    return render(request, "modules_list.html", context)


@lru_cache()
def index(request):
    return render(request, "home.html")
