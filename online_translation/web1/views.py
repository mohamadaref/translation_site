from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


User = get_user_model()

def accept_job(request):
    pass

def profile(request):
    if request.user.is_authenticated == True:
        myUser = User.objects.get(username = request.user)
        context = {}
        context['username'] = myUser.username
        context['email'] = myUser.email
        context['ProfileImage'] = myUser.ProfileImage
        return render(request , 'app/profile.html' , context)
    else:
        return HttpResponse("you're not loged in!")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Create your views here.
