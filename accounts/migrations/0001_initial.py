# Generated by Django 4.2.7 on 2023-11-11 13:45

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vaccination_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_number', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_pics)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('job_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccination_store.jobplace')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]