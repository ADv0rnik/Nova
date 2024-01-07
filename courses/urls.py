from django.urls import path

from .views import CoursesView, CourseDetailView


urlpatterns = [
    path("", CoursesView.as_view(), name="course_list"),
    path("<slug:course_slug>/info", CourseDetailView.as_view(), name="course_details"),
]
