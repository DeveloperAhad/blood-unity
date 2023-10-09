# Generated by Django 3.2.10 on 2023-10-08 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0003_chatroom_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatroom',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
