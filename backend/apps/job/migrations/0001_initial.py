# Generated by Django 3.2.9 on 2022-07-10 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Управление')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Менеджеры')),
            ],
            options={
                'verbose_name': 'Управление',
                'verbose_name_plural': 'Управления',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Отдел')),
                ('management', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='job.management', verbose_name='Управление')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='managers', to=settings.AUTH_USER_MODEL, verbose_name='Менеджеры')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
    ]
