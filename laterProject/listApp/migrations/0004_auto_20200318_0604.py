# Generated by Django 3.0.1 on 2020-03-18 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0003_auto_20200317_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='author_first_name',
            new_name='author_name',
        ),
        migrations.RemoveField(
            model_name='books',
            name='author_last_name',
        ),
    ]
