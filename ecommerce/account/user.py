# Code by Prasoon Naithani

from django import forms
from django.contrib.auth import models, authenticate, get_user, get_user_model

from django.contrib.auth.models import User, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2",'first_name','last_name','email']

class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': '', 'last_name' : '', 'email' : ''}    











    

