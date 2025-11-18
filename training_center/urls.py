from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns, set_language
from users import views as user_views  # <-- добавлено
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from main.sitemaps import StaticViewSitemap, EmployerSitemap, UserProfileSitemap
from main.views import SitemapView


# serve robots + sitemap (dev). In production serve directly by webserver.
sitemaps_dict = {
    'static': StaticViewSitemap,
    'employers': EmployerSitemap,
    'users': UserProfileSitemap,
}



urlpatterns = [
   
    path('i18n/setlang/', set_language, name='set_language'),
]

# Остальные маршруты можно обернуть в i18n_patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('candidates/', include('candidates.urls')),
   path('employers/', include('employer.urls', namespace='employer')),  # namespace
    path('jobs/', include('Job.urls')),
    path('users/', include('users.urls')),
    path('register/', user_views.register, name='register'),  # <-- добавлено
    path('sitemap.xml', SitemapView.as_view(), name='sitemap'),
    
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)