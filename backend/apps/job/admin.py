from django.contrib import admin

from backend.apps.job.models import Government, Department


@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
