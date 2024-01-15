# Generated by Django 5.0.1 on 2024-01-15 16:52

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_alter_women_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='women',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=1),
        ),
    ]