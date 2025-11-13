from django.contrib import admin
from .models import Employer

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'user')  # показываем поля в списке
    search_fields = ('company_name', 'position', 'user__username')  # поиск по этим полям
    list_filter = ('position',)  # фильтры в админке
