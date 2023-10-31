from django.urls import path, re_path
from .views import (
    RegisterView,
    login_user,
    logout_user,
)

urlpatterns = [
    re_path("^login/", login_user, name="login"),
    re_path("^logout/", logout_user, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
