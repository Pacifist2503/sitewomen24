# Generated by Django 5.0.1 on 2024-01-20 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0008_husband_women_husband'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_created'], 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts_cat', to='women.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='women',
            name='husband',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='women', to='women.husband', verbose_name='Муж'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='women',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts_tag', to='women.tagpost', verbose_name='Тэги'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='women',
            name='time_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
