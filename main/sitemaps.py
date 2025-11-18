# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from employer.models import Employer
from users.models import CustomUser  # если у тебя кастомная модель User

LANGUAGES = ['ru', 'en', 'de']  # доступные языки

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['index', 'employer:employer_list', 'users:login', 'users:register']

    def location(self, item):
        return reverse(item)

    def alternate_links(self):
        # для hreflang
        links = {}
        for lang in LANGUAGES:
            links[lang] = f"/{lang}/"
        return links


class EmployerSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Employer.objects.all()

    def lastmod(self, obj):
        return getattr(obj, 'created_at', timezone.now())

    def location(self, obj):
        return reverse('employer:employer_detail', args=[obj.id])

    def alternate_links(self, obj):
        links = {}
        for lang in LANGUAGES:
            links[lang] = f"/{lang}/employers/{obj.id}/"
        return links


class UserProfileSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        return CustomUser.objects.filter(is_active=True)

    def location(self, obj):
        return reverse('users:profile', args=[obj.id])

    def lastmod(self, obj):
        return getattr(obj, 'date_joined', timezone.now())

    def alternate_links(self, obj):
        links = {}
        for lang in LANGUAGES:
            links[lang] = f"/{lang}/users/profile/{obj.id}/"
        return links
