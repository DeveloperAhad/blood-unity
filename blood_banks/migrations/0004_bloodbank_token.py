# Generated by Django 3.2.10 on 2024-01-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_banks', '0003_auto_20240112_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbank',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
