from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models

from backend.apps.accounts.managers import UserManager
from backend.apps.job.models import Department, Government


class User(AbstractUser):
    ROLE_DIRECTOR = 'Директор'
    ROLE_MANAGER = 'Менеджер'
    ROLE_STAFF = 'Специалист'
    ROLES = (
        (ROLE_DIRECTOR, 'Директор'),
        (ROLE_MANAGER, 'Менеджер'),
        (ROLE_STAFF, 'Специалист'),
    )

    username = models.CharField('Логин', max_length=150, unique=True)
    role = models.CharField('Роль', choices=ROLES, default=ROLE_STAFF, max_length=50)
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    email = None
    avatar = models.ImageField("Фото", upload_to="user_images/", null=True, blank=True)
    is_active = models.BooleanField('Работает', default=False)
    phone = models.CharField(
        'Номер телефона',
        null=True,
        blank=True,
        max_length=10,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()


class DirectorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='director', verbose_name='Сотрудник')
    government = models.ForeignKey(Government, on_delete=models.PROTECT, related_name='directors', verbose_name='Отдел')

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager', verbose_name='Сотрудник')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='managers', null=True,
                                   verbose_name='Отдел')

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker', verbose_name='Сотрудник')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='workers', null=True, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'



