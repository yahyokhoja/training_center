from django.shortcuts import render
from django.http import HttpResponse

def employer_list(request):
    return HttpResponse("Список работодателей")

def employer_detail(request, id):
    return HttpResponse(f"Детали работодателя {id}")


# Create your views here.
