import logging

from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView
from django.conf import settings
from django_email_verification import send_email

from .decorators import unauthenticated_user
from .forms import CreateUserForm
from .utils import email_verification_token

logger = logging.getLogger("asnova")
logger.event_source = __name__


class RegisterView(FormView):
    form_class = CreateUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["first_name"]
            # email = form.cleaned_data["email"]
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_email(user)
            return HttpResponseRedirect(reverse('login'))
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

    # def send_email(self, user, **kwargs):
    #     current_site = get_current_site(self.request)
    #     contact_username = kwargs.get("name")
    #     contact_email = kwargs.get("email")
    #     subject = f"Greetings from AsvetaNova"
    #     message = f"Dear {contact_username}. Please activate your account"
    #     body = render_to_string(
    #         "email_body.html",
    #         {
    #             "domain": current_site.domain,
    #             "uid": urlsafe_base64_encode(force_bytes(user.pk)),
    #             "token": email_verification_token.make_token(user),
    #             "message": message,
    #         },
    #     )
    #     EmailMessage(
    #         subject=subject,
    #         body=body,
    #         from_email=settings.EMAIL_HOST_USER,
    #         to=[contact_email],
    #     ).send()


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

# TODO: Render success page after sending email
