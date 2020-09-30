from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .user import RegistrationForm

def index(request):
    return HttpResponse("This is Home")

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        userAuthentication = authenticate(request, username = username, password = password)
        
        if userAuthentication is not None:
            login(request,userAuthentication)
            return redirect('home')
        else:
            preFilledForm = AuthenticationForm(request.POST)
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
            return render(request, 'registration.html', {'form': createForm})
    else:
        createForm = RegistrationForm()
    return render(request, 'registration.html',{'form':createForm})
