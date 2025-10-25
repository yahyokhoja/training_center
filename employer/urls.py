from django.urls import path
from . import views

urlpatterns = [
    path('', views.employer_list, name='employer_list'),
    path('<int:id>/', views.employer_detail, name='employer_detail'),
]
