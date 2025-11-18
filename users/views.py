from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django import forms
from .forms import CustomUserCreationForm, UserProfileEditForm


User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, max_length=20)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email', '')
        user.phone = self.cleaned_data.get('phone', '')
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _("Вы успешно зарегистрированы!"))
            return redirect('users:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:profile')
        messages.error(request, _("Неверное имя пользователя или пароль."))
    else:
        form = LoginForm(request=request)
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _("Профиль успешно обновлён!"))
            return redirect('main:index')
        else:
            # Вывести все ошибки формы (включая не-полевые)
            for field, errors in form.errors.items():
                label = form.fields[field].label if field in form.fields else ""
                for error in errors:
                    if label:
                        messages.error(request, f"{label}: {error}")
                    else:
                        messages.error(request, error)
    else:
        form = UserProfileEditForm(instance=request.user)
    return render(request, 'users/profile_edit.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, _("Вы вышли из аккаунта."))
    return redirect('users:login')
