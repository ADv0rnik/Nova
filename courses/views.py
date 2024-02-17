import logging
from functools import lru_cache

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Course
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

    # TODO: Needs to optimize queries to database

    def get_context_data(self, *, object_list=None, **kwargs):
        user_id = self.request.user.id
        profile = Profile.objects.get(user__id=user_id)
        is_course_result = False

        if course_results := CourseResults.objects.filter(profile__id=profile.id):
            for course_result in course_results:
                if course_result.course.slug == self.kwargs["course_slug"]:
                    is_course_result = True
                    break

        context = super().get_context_data(**kwargs)
        context["modules"] = context["course"].course_module.all()
        context["is_course_result"] = is_course_result

        return context


def get_module_list(request, course_slug):
    user_id = request.user.id
    profile = Profile.objects.get(user__id=user_id)
    course = Course.objects.get(slug=course_slug)

    if course_results := CourseResults.objects.filter(profile__id=profile.id):
        for course_result in course_results:
            if course_result.course.slug == course_slug:
                break
        else:
            create_course_result(profile, course)
    else:
        create_course_result(profile, course)

    modules = course.course_module.all()
    context = {
        "course": course,
        "modules": modules,
    }
    return render(request, "modules_list.html", context)


def create_course_result(profile: Profile, course: Course, passed=False):
    course_results = CourseResults(profile=profile, course=course, passed=passed)
    course_results.save()


@lru_cache()
def index(request):
    return render(request, "home.html")
