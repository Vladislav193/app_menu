# Generated by Django 5.1.1 on 2024-09-26 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название меню')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название пункта')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='URL (если не указано, используется named url)')),
                ('named_url', models.CharField(blank=True, max_length=100, verbose_name='Named URL')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.menu', verbose_name='Меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuitem', verbose_name='Родительский элемент')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
                'ordering': ['order'],
            },
        ),
    ]
