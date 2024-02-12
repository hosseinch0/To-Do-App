from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('/')
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'authentication/signin.html', context)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {"form": form}
        return render(request, 'authentication/signup.html', context)
