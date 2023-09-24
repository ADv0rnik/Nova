import logging

from django.shortcuts import render
from django.views.generic import ListView

from .models import Course


logger = logging.getLogger("adukar")
logger.event_source = __name__


class CoursesView(ListView):
    model = Course
    template_name = "courses.html"
    queryset = Course.objects.all()
    context_object_name = "courses"
    logger.debug(
        "start application",
        extra={"event_name": "courses_view", "event_source": logger.event_source},
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Courses list"
        return context


def index(request):
    return render(request, 'home.html')
