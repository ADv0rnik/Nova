from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView

from .decorators import unauthenticated_user
from .forms import CreateUserForm
from .utils import email_verification_token


class RegisterView(FormView):
    form_class = CreateUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def _send_email_verification(self, user):
        current_site = get_current_site(self.request)
        subject = "Activate your account"
        body = render_to_string(

        )


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
