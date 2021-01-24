# Code by Prasoon Naithani

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .user import RegistrationForm, ProfileForm
from .models import Featured

def index(request):
    clearingMessage(request)
    return render(request,"index.html",{})

def featuredProducts(request):
    featuringProducts = Featured.objects.all()
    return render(request, 'index.html', {'featured': featuringProducts})

def userLogin(request):
    if request.method == 'POST':
        clearingMessage(request)
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        userAuthentication = authenticate(request, username = username, password = password)
        
        if userAuthentication is not None:
            clearingMessage(request)
            login(request,userAuthentication)
            return redirect('home')
        else:
            preFilledForm = AuthenticationForm(request.POST)
            messages.error(request, 'Username or Password is incorrect.')
            return render(request, 'login.html', {'signform': preFilledForm})
    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'signform':form})


def createUser(request):
    if request.method == 'POST':
        createForm = RegistrationForm(request.POST)
        if createForm.is_valid():
            createForm.save()
            username = createForm.cleaned_data.get('username')
            password = createForm.cleaned_data.get('password1')
            userAuthentication = authenticate(request, username = username, password = password)
            login(request,userAuthentication)
            return redirect('home')
        else:
            if(len(createForm.cleaned_data.get('password1')) < 6):
                messages.error(request, "Passwords should be of atleast 6 characters.")      
            elif(createForm.cleaned_data.get('password1') != createForm.cleaned_data.get('password2')):
                messages.error(request, "Passwords didn't match. Try again.")
            else:
                messages.error(request, "Oops something went wrong. Please try again.")
            return render(request, 'registration.html', {'form': createForm})
    else:
        createForm = RegistrationForm()
    return render(request, 'registration.html',{'form':createForm})

def clearingMessage(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass

def userLogout(request):
    logout(request)
    return redirect("login")

@login_required
def userAccount(request):
    if request.user.is_authenticated:
        profile_personalForm = ProfileForm(instance=request.user)
        profile_changePassword = PasswordChangeForm(user=request.user)
        if request.method == 'POST': 
            if 'personalInfo' in request.POST:
                profile_personalForm = ProfileForm(request.POST, instance=request.user)
                if profile_personalForm.is_valid():
                    profile_personalForm.save()
            elif 'changePassword' in request.POST:
                profile_changePassword = PasswordChangeForm(data=request.POST, user=request.user)
                if profile_changePassword.is_valid():
                    profile_changePassword.save()
                    update_session_auth_hash(request, profile_changePassword.user)
                    messages.success(request, 'Password Successfully Changed')
                    redirect('account')

        return render(request, 'account.html', {'profileForm' : profile_personalForm, 'passwordChange': profile_changePassword})
        
    else:
        return redirect('login')



    


