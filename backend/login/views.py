from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from login.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


def LoginUser(request):
    if request.method=="POST":
        forms = AuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request,user)
            return redirect('index')
        

    
    return render(request ,'usuarios/login.html')

def RegisterUser(request):
    erro = ""
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            if form.errors:

                erro = form.errors
                print(form.errors)
                
    else:
        form = RegisterForm()
    context={
        "form":form,
        "erro":erro,
    }
    return render(request ,'usuarios/register.html',context )


def SalirUser(request):
    logout(request)
    return redirect('index')
