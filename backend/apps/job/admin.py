from django.contrib import admin

from backend.apps.accounts.models import WorkerProfile, ManagerProfile
from backend.apps.job.models import Management, Department


class WorkerProfileInline(admin.StackedInline):
    model = WorkerProfile
    can_delete = False
    verbose_name_plural = "Работники"
    fk_name = "department"


class ManagerProfileInline(admin.StackedInline):
    model = ManagerProfile
    can_delete = False
    verbose_name_plural = "Менеджеры"
    fk_name = "department"


@admin.register(Management)
class GovernmentAdmin(admin.ModelAdmin):
    inlines = [ManagerProfileInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [WorkerProfileInline]
