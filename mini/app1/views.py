from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import RegisterForm
# from django.contrib.auth import logout
from django.contrib.auth.models import User


# from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request, 'index.html')


    return render(request, 'register.html', {'form': form})


def about(request):
    return render(request,'about.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # This calls Django's login, not your view
            return redirect('index')  # or wherever you want
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, "Registration successful. You can login now.")
            return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)  # This is Django's logout function
    return redirect('login') 
