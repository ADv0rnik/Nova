import logging

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django_email_verification import send_email
from .decorators import unauthenticated_user
from .forms import CreateUserForm


logger = logging.getLogger("asnova")
logger.event_source = __name__


class RegisterView(FormView):
    form_class = CreateUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_email(user)
            return HttpResponseRedirect(reverse("login"))
        else:
            logger.debug(
                f"Form error: {form.errors.as_json()}",
                extra={
                    "event_name": "register_view",
                    "event_source": logger.event_source,
                },
            )
            form = self.form_class()
        return render(request, self.template_name, {"form": form})


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password do not match")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return render(request, "home.html")


# TODO: Реализовать функционал редиректа на страницу профиля после регистрации,
#  т.к. аутентификация происходит автоматически.
