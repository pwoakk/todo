# Generated by Django 3.2.9 on 2022-06-15 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Отдел', 'verbose_name_plural': 'Отделы'},
        ),
        migrations.AlterModelOptions(
            name='government',
            options={'verbose_name': 'Управление', 'verbose_name_plural': 'Управления'},
        ),
        migrations.RemoveField(
            model_name='government',
            name='managers',
        ),
    ]
