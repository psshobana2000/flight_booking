# Generated by Django 5.0.3 on 2024-09-09 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='confirm_password',
        ),
    ]
