from django.urls import path, re_path
from .views import RegisterView, login_user
# from.views import register_user


urlpatterns = [
    re_path("^login/", login_user, name="login"),
    path("register/", RegisterView.as_view(), name="register")
]
