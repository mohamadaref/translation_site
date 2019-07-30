from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

def accept_job(request):
    pass

def profile(request):
    if request.user.is_authenticated == True:
        myUser = CustomUser.objects.get(username = request.user)
        context = {}
        context['username'] = myUser.username
        context['email'] = myUser.email
        context['ProfileImage'] = myUser.ProfileImage 
        return render(request , 'app/profile.html' , context)
    else:
        return HttpResponse("you're not login!")

# Create your views here.
