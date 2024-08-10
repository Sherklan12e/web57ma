from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

def LoginUser(request):
    return render(request ,'usuarios/login.html')

def RegisterUser(request):
    return render(request ,'usuarios/register.html')
def SalirUser(request):
    logout(reqeust)
    return redirect('index')
