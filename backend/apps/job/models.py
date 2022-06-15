from django.db import models


class Government(models.Model):
    name = models.CharField('Управление', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Отдел', max_length=50, unique=True)
    government = models.ForeignKey(Government,on_delete=models.CASCADE, related_name='department', verbose_name='Управление')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

