from django.contrib import admin
from .models import CV, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # сколько пустых полей для навыков показывать
    min_num = 0
    verbose_name = "Навык"
    verbose_name_plural = "Навыки"


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "age")
    search_fields = ("full_name", "user__username")
    inlines = [SkillInline]
