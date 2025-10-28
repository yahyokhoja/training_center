from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns, set_language
from django.conf.urls.i18n import set_language  # <-- импортируем сюда
urlpatterns = [
     path('i18n/setlang/', set_language, name='set_language'),
    
]
# Остальные маршруты можно обернуть в i18n_patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('candidates/', include('candidates.urls')),
    path('employers/', include('employer.urls')),
    path('jobs/', include('Job.urls')),
    path('users/', include('users.urls')),  # ✅ подключаем приложение
)