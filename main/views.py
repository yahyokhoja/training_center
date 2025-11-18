from django.shortcuts import render
from django.views.generic import TemplateView
from employer.models import Employer
from users.models import CustomUser

def index(request):
    return render(request, 'main/index.html')  # путь к твоему шаблону

class SitemapView(TemplateView):
    template_name = "sitemap.xml"
    content_type = "application/xml"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = ['ru', 'en', 'de']
        context['static_urls'] = ['/', '/employers/', '/users/login/', '/users/register/']
        context['employers'] = Employer.objects.all()
        context['users'] = CustomUser.objects.filter(is_active=True)
        return context