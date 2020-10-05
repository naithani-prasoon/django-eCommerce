# Code by Prasoon Naithani

from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User, User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2",'first_name','last_name','email']









    

