# Generated by Django 4.1.1 on 2022-10-21 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0003_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
