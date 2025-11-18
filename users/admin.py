from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Поля, отображаемые в списке пользователей
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role',)  # 'role' добавлен

    # Поля для редактирования существующего пользователя
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'role')}),
    )

    # Поля при создании нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'role')}),
    )

    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)
