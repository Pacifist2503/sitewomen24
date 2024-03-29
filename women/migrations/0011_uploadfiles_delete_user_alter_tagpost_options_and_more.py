# Generated by Django 5.0.1 on 2024-01-30 11:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_alter_women_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterModelOptions(
            name='tagpost',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterModelManagers(
            name='women',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, default='None', null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='women',
            name='husband',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='women', to='women.husband', verbose_name='Муж'),
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5, 'Минимум 5 символов'), django.core.validators.MaxLengthValidator(100, message='Максимум 5 символов')], verbose_name='Слаг'),
        ),
    ]
