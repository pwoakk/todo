from django.db import models


class Management(models.Model):
    name = models.CharField(max_length=100, verbose_name='Управление')
    manager = models.ForeignKey('accounts.User', on_delete=models.PROTECT, verbose_name='Менеджеры')

    class Meta:
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Отдел', max_length=50, unique=True)
    manager = models.ForeignKey('accounts.User',
                                on_delete=models.PROTECT,
                                verbose_name='Менеджеры',
                                related_name='managers')
    management = models.ForeignKey(Management, on_delete=models.CASCADE, related_name='worker', verbose_name='Управление')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

