# Generated by Django 3.2.10 on 2024-01-12 13:56

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_users', '0002_auto_20230709_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaluser',
            name='last_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
