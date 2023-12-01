import logging

from django.shortcuts import render
from django.views.generic import ListView

from .models import Course


logger = logging.getLogger("adukar")
logger.event_source = __name__


class CoursesView(ListView):
    model = Course
    template_name = "courses.html"
    queryset = Course.objects.defer('created_at', 'updated_at').prefetch_related
    context_object_name = "courses"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Courses list"
        return context


def index(request):
    return render(request, "home.html")
