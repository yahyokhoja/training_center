from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'users'

urlpatterns = [
    path('', lambda request: redirect('users:login')),  # редирект с /users/ на /users/login/
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
