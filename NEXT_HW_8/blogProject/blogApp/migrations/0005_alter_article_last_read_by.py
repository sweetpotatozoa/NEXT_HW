# Generated by Django 5.0.3 on 2024-04-21 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_article_last_read_by_article_last_read_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_read_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
