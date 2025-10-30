from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model  


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect('login')
