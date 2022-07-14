from django.db import models

from backend.apps.accounts.models import User


class Notepad(models.Model):
    text = models.TextField('Задание')
    author = models.ForeignKey(User, related_name='notepad', verbose_name='Автор', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Блокнот'
        verbose_name_plural = 'Блокнот'
        ordering = ['created']

    def __str__(self):
        return f'{self.text[:35]}'

