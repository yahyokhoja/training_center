from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),          # Главная страница
    path('candidates/', include('candidates.urls')),
    path('employers/', include('employer.urls')),
    path('jobs/', include('Job.urls')),
]
