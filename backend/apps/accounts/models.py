from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models

from backend.apps.accounts.managers import UserManager
from backend.apps.job.models import Department, Management


class User(AbstractUser):
    ROLE_MANAGER = 'Менеджер'
    ROLE_STAFF = 'Специалист'
    ROLES = (
        (ROLE_MANAGER, 'Менеджер'),
        (ROLE_STAFF, 'Специалист'),
    )

    username = models.CharField('Логин', max_length=150, unique=True)
    role = models.CharField('Роль', choices=ROLES, default=ROLE_STAFF, max_length=50)
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    email = None
    avatar = models.ImageField("Фото", upload_to="user_images/", null=True, blank=True, default='./default.png')
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

    @property
    def get_photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "default.png"


class ManagerProfile(models.Model):
    POSITION_DIRECTOR = 'Директор'
    POSITION_MANAGER = 'Менеджер'
    POSITION_OTHER = 'Другое'
    POSITION_STATUS = (
        (POSITION_DIRECTOR, 'Директор'),
        (POSITION_MANAGER, 'Менеджер'),
        (POSITION_OTHER, 'Другое'),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='manager',
        verbose_name='Сотрудник',)
    department = models.ForeignKey(Management, on_delete=models.PROTECT, related_name='managers', null=True,
                                   verbose_name='Управление')
    position = models.CharField('Должность', max_length=40, choices=POSITION_STATUS, default=POSITION_OTHER)

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.middle_name}'


class WorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='worker',
                                verbose_name='Сотрудник',)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='workers', null=True, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.middle_name}'



