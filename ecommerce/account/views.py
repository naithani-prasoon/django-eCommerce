from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        userAuthentication = authenticate(request, username = username, password = password)
        
        if userAuthentication is not None:
            login(request,userAuthentication)
            redirect('registration.html')
        else:
            preFilledForm = AuthenticationForm(request.POST)
            return redirect(request, 'login.html', {'form': preFilledForm})
    else:
        form = AuthenticationForm()
    
    return render(request,'login.html',{'signform':form})


def createUser(request):
    if request.method == 'POST':
        createForm = UserCreationForm(request.POST)
        if createForm.is_valid():
            createForm.save()
            username = request.POST['username']
            password = request.POST['password']
            userAuthentication = authenticate(request, username = username, password = password)
            login(request,userAuthentication)
            return redirect('admin')
        else:
            return render(request, 'registration.html', {'form': createForm})
    else:
        createForm = UserCreationForm()
    return render(request, 'registration.html',{'form':createForm})
