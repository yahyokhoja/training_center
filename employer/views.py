from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Employer
from .forms import EmployerForm

# 🔹 Список всех работодателей
def employer_list(request):
    employers = Employer.objects.all()
    return render(request, 'employer/employer_list.html', {'employers': employers})

# 🔹 Детали конкретного работодателя
def employer_detail(request, id):
    employer = get_object_or_404(Employer, id=id)
    return render(request, 'employer/employer_detail.html', {'employer': employer})

# 🔹 Создание нового профиля работодателя
@login_required
def employer_create(request):
    if hasattr(request.user, 'employer_profile'):
        # Пользователь уже создал профиль
        return redirect('employer:employer_detail', id=request.user.employer_profile.id)

    if request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            employer = form.save(commit=False)
            employer.user = request.user  # 🔹 привязка к текущему пользователю
            employer.save()
            return redirect('employer:employer_detail', id=employer.id)
    else:
        form = EmployerForm()
    return render(request, 'employer/employer_form.html', {'form': form})

# 🔹 Обновление профиля (только владелец)
@login_required
def employer_update(request, id):
    employer = get_object_or_404(Employer, id=id)
    if employer.user != request.user:
        return redirect('employer:employer_detail', id=employer.id)

    if request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES, instance=employer)
        if form.is_valid():
            form.save()
            return redirect('employer:employer_detail', id=employer.id)
    else:
        form = EmployerForm(instance=employer)
    return render(request, 'employer/employer_form.html', {'form': form})

# 🔹 Удаление профиля (только владелец)
@login_required
def employer_delete(request, id):
    employer = get_object_or_404(Employer, id=id)
    if employer.user != request.user:
        return redirect('employer:employer_detail', id=employer.id)

    if request.method == 'POST':
        employer.delete()
        return redirect('employer:employer_list')

    return render(request, 'employer/employer_confirm_delete.html', {'employer': employer})
