from django.contrib import admin

from backend.apps.accounts.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
