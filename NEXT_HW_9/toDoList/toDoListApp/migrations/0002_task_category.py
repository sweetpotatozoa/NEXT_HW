# Generated by Django 5.0.4 on 2024-04-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoListApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default='작업', max_length=20),
        ),
    ]