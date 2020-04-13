from django.shortcuts import render,redirect,get_object_or_404
from .models import Reviews

# Create your views here.
def index(request):
    reviews=Reviews.objects.all()
    context={
        'reviews':reviews
    }
    return render(request,'reviews/index.html',context)