from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from decorators import unauthenticated_user


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
