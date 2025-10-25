from django.shortcuts import render
from django.http import HttpResponse

def candidate_list(request):
    return HttpResponse("Список кандидатов")

def candidate_detail(request, id):
    return HttpResponse(f"Профиль кандидата {id}")


# Create your views here.
