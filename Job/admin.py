from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'employer__username')
