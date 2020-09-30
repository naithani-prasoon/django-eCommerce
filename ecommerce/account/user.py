from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password1'
        ]


    

