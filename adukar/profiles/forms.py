from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import EmailField
from django.forms.forms import Form
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']