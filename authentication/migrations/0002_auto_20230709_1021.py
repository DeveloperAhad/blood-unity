# Generated by Django 3.2.10 on 2023-07-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='account',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='account',
            name='gender',
        ),
    ]
