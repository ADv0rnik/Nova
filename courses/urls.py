from django.urls import path

from .views import CoursesView


app_name = "courses"
urlpatterns = [path("", CoursesView.as_view(), name="course_list")]
