from django.db import models
from django.utils import timezone

from backend.apps.accounts.models import User
from backend.apps.job.models import Department


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Task(models.Model):
    """Модель задач пользователя"""

    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=one_week_hence)

    STATUS_NOT_STARTED = 'not_started'
    STATUS_IN_PROCESS = "in_process"
    STATUS_FINISHED = "finished"
    TASK_STATUSES = {
        (STATUS_NOT_STARTED, "Не_начата"),
        (STATUS_IN_PROCESS, "Выполняется"),
        (STATUS_FINISHED, "Завершена")
    }

    status = models.CharField("Статус", max_length=11,
                              choices=TASK_STATUSES, default=STATUS_NOT_STARTED)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name='tasks', verbose_name='Задачи')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['created']

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Моделька тега для задач, будет использоваться для фильтрации задач"""
    name = models.CharField('Наименование', max_length=30, unique=True)
    slug = models.SlugField('Слаг', max_length=30, unique=True)
    task = models.ManyToManyField(Task)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Модель комментария/заметки к задаче"""
    text = models.TextField('Комментарий')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text[:20]}'
