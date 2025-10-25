from django.shortcuts import render
from django.http import HttpResponse

def job_list(request):
    return HttpResponse("Список вакансий")

def job_detail(request, id):
    return HttpResponse(f"Информация о вакансии {id}")


# Create your views here.
