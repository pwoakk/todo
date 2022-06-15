from django.contrib import admin
from .models import *

from backend.apps.accounts.models import WorkerProfile, ManagerProfile, DirectorProfile

class WorkerProfileInline(admin.StackedInline):
    model = WorkerProfile
    can_delete = False
    verbose_name_plural = "Работники"
    fk_name = "user"

class ManagerProfileInline(admin.StackedInline):
    model = ManagerProfile
    can_delete = False
    verbose_name_plural = "Менеджеры"
    fk_name = "user"


class DirectorProfileInline(admin.StackedInline):
    model = DirectorProfile
    can_delete = False
    verbose_name_plural = "Директоры"
    fk_name = "user"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'first_name',
        'middle_name',
        'last_name',
        'phone',
        'is_active',
        'role'
    ]
    list_editable = ['is_active']

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     inline_instances = []
    #     if obj.role == User.ROLE_DIRECTOR:
    #         inline = DirectorProfileInline(self.model, self.admin_site)
    #     elif obj.role == User.ROLE_MANAGER:
    #         inline = ManagerProfileInline(self.model, self.admin_site)
    #     else:
    #         inline = WorkerProfileInline(self.model, self.admin_site)
    #     inline_instances.append(inline)
    #     return inline_instances
    #
    # def get_formsets(self, request, obj=None):
    #     for inline in self.get_inline_instances(request, obj):
    #         #                                           ^^^^^ this is new
    #         yield inline.get_formset(request, obj)
