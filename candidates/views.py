from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CV, Skill
from .forms import CVForm, SkillForm


# ==================================
# CV CREATE
# ==================================
@login_required
def cv_create(request):
    if hasattr(request.user, "cv"):
        return redirect("candidates:cv_detail", pk=request.user.cv.pk)

    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            return redirect("candidates:cv_detail", pk=cv.pk)
    else:
        form = CVForm()

    return render(request, "candidates/cv_form.html", {"form": form})


# ==================================
# CV DETAIL
# ==================================
@login_required
def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk, user=request.user)
    return render(request, "candidates/cv_detail.html", {"cv": cv})


# ==================================
# CV UPDATE
# ==================================
@login_required
def cv_edit(request, pk):
    cv = get_object_or_404(CV, pk=pk, user=request.user)

    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            form.save()
            return redirect("candidates:cv_detail", pk=cv.pk)
    else:
        form = CVForm(instance=cv)

    return render(request, "candidates/cv_form.html", {"form": form})


# ==================================
# CV DELETE
# ==================================
@login_required
def cv_delete(request, pk):
    cv = get_object_or_404(CV, pk=pk, user=request.user)
    cv.delete()
    return redirect("users:profile")


# ==================================
# SKILL ADD
# ==================================
@login_required
def skill_add(request, cv_pk):
    cv = get_object_or_404(CV, pk=cv_pk, user=request.user)

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.cv = cv
            skill.save()
            return redirect("candidates:cv_detail", pk=cv.pk)
    else:
        form = SkillForm()

    return render(request, "candidates/skill_form.html", {"form": form})


# ==================================
# SKILL DELETE
# ==================================
@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, cv__user=request.user)
    cv_pk = skill.cv.pk
    skill.delete()
    return redirect("candidates:cv_detail", pk=cv_pk)
