# Generated by Django 5.1.6 on 2025-03-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва')),
                ('text', models.TextField(verbose_name='Текст')),
                ('reminder', models.DateTimeField(blank=True, null=True, verbose_name='Нагадування')),
                ('category', models.CharField(choices=[('Робота', 'Робота'), ('Особисте', 'Особисте'), ('Навчання', 'Навчання')], max_length=50, verbose_name='Категорія')),
            ],
        ),
    ]
