from django.urls import path
from . import views

app_name = 'employer'  # 🔹 важный момент для namespace

urlpatterns = [
    path('', views.employer_list, name='employer_list'),
    path('create/', views.employer_create, name='employer_create'),
    path('<int:id>/', views.employer_detail, name='employer_detail'),
    path('<int:id>/edit/', views.employer_update, name='employer_update'),
    path('<int:id>/delete/', views.employer_delete, name='employer_delete'),
]
