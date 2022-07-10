from django.contrib import admin

from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status', 'created', 'updated', 'deadline', ]
    list_filter = ['status']
    search_fields = ('id', 'name', 'description', 'status', 'created', 'deadline', )


@admin.register(Project)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
