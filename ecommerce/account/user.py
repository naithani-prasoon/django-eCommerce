from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password1'
        ]