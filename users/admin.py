from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Поля, отображаемые в списке пользователей
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')  # 'role' убран, так как его нет

    # Поля для редактирования существующего пользователя
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )

    # Поля при создании нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}),
    )

    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)
