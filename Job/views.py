from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm


# ===== LIST =====
def job_list(request):
    jobs = Job.objects.all()
    return render(request, "Job/job_list.html", {"jobs": jobs})


# ===== DETAIL =====
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, "Job/job_detail.html", {"job": job})


# ===== CREATE =====
@login_required
def create_job(request):
    if request.user.role != "employer":
        return redirect("Job:job_list")

    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect("Job:job_detail", pk=job.pk)
    else:
        form = JobForm()

    return render(request, "Job/job_form.html", {"form": form, "title": "Создать вакансию"})


# ===== UPDATE =====
@login_required
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.user != job.employer:
        return redirect("Job:job_detail", pk=pk)

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("Job:job_detail", pk=pk)
    else:
        form = JobForm(instance=job)

    return render(request, "Job/job_form.html", {"form": form, "title": "Редактировать вакансию"})


# ===== DELETE =====
@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.user != job.employer:
        return redirect("Job:job_detail", pk=pk)

    if request.method == "POST":
        job.delete()
        return redirect("Job:job_list")

    return render(request, "Job/job_confirm_delete.html", {"job": job})
