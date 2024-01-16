# Generated by Django 5.0.1 on 2024-01-16 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_alter_women_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='women',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts_cat', to='women.category'),
        ),
        migrations.AddField(
            model_name='women',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts_tag', to='women.tagpost'),
        ),
    ]