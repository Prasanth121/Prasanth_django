from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import loginInfo
# Create your views here.

def login(request):
    form=loginInfo(request.POST)
    return render(request,'registration/login.html',{'form':form})

def profile(request):
    if request.method=='POST':
        if request.POST.get('username')=="prasanth" and request.POST.get('password')=="prasanth":
            return render(request,'profile.html')
        else:
            return render(request,'login.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

def index(request):
    return render(request,'index.html')