# Generated by Django 3.2.9 on 2022-07-10 16:42

import backend.apps.accounts.models
import backend.apps.task.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(default=backend.apps.task.models.one_week_hence)),
                ('status', models.CharField(choices=[('Не начат', 'Не_начата'), ('Завершен', 'Завершена'), ('В процессе', 'Выполняется')], default='Не начат', max_length=11, verbose_name='Статус')),
                ('author', models.ForeignKey(default=backend.apps.accounts.models.ManagerProfile, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='accounts.managerprofile', verbose_name='Задачи')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.department', verbose_name='Отдел')),
                ('performer', models.ForeignKey(default=backend.apps.accounts.models.WorkerProfile, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performer_task', to='accounts.workerprofile')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Слаг')),
                ('task', models.ManyToManyField(to='task.Task')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='task.task')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
