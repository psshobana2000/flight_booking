# Generated by Django 5.0.3 on 2024-08-19 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_remove_adminlogin_ph_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='tour_package',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='report',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='report',
            name='trip',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
