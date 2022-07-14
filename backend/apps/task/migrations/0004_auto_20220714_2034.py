# Generated by Django 3.2.9 on 2022-07-14 14:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_auto_20220713_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='performer',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Не начат', 'Не_начата'), ('Завершен', 'Завершена'), ('В процессе', 'Выполняется')], default='Не начат', max_length=11, verbose_name='Статус'),
        ),
    ]