# Generated by Django 2.2.7 on 2020-04-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0008_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(default='This book is about.....', max_length=4000),
        ),
    ]
