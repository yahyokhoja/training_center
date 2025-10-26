from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'main/profile.html')
from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')
