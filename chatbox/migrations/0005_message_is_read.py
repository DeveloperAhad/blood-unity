# Generated by Django 3.2.10 on 2023-10-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0004_auto_20231008_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
