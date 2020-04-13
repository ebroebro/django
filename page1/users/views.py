from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User=get_user_model()

# Create your views here.
def index(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,'users/index.html',context)


def signup(request):
    if request.method=='POST':
        form=UserCreationForm()
        if form.is_valid():
            form.save()
            return redirect('users:index')
    else:
        form=UserCreationForm()
    context={
        'form':form
    }
    return render(request,'users/signup.html',context)