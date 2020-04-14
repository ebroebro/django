from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
User=get_user_model()

def index(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request, 'accounts/index.html',context)

def create(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form=UserCreationForm()
    context={
        'form':form
    }
    return render(request,'accounts/create.html',context)

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid:
            auth_login(request,form.get_user())
            return redirect('community:index')
    else:
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')