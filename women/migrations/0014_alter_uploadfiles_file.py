# Generated by Django 5.0.2 on 2024-02-18 20:32

import women.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0013_uploadfiles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file',
            field=models.FileField(upload_to=women.models.user_directory_path),
        ),
    ]
