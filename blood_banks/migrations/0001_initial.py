# Generated by Django 3.2.10 on 2023-10-07 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('address', models.CharField(max_length=100, null=True)),
                ('blood_group_a_positive', models.IntegerField(default=0)),
                ('blood_group_a_negative', models.IntegerField(default=0)),
                ('blood_group_b_positive', models.IntegerField(default=0)),
                ('blood_group_b_negative', models.IntegerField(default=0)),
                ('blood_group_o_positive', models.IntegerField(default=0)),
                ('blood_group_o_negative', models.IntegerField(default=0)),
                ('blood_group_ab_positive', models.IntegerField(default=0)),
                ('blood_group_ab_negative', models.IntegerField(default=0)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.district')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.division')),
                ('union', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.union')),
                ('upazila', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.upazila')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
