from django.urls import path

from .views import CoursesView, CourseDetailView, get_module_list


urlpatterns = [
    path("", CoursesView.as_view(), name="course_list"),
    path("<slug:course_slug>/info", CourseDetailView.as_view(), name="course_details"),
    path("<slug:course_slug>/modules", get_module_list, name="modules_content"),
]
