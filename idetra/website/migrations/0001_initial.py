# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators
import website.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, verbose_name='Your Name', blank=True)),
                ('lastname', models.CharField(max_length=120, verbose_name='Your last name', blank=True)),
                ('middlenames', models.CharField(max_length=120, verbose_name='Your middle name(s)', blank=True)),
                ('picture', models.ImageField(height_field=b'height_field', upload_to=website.models.upload_location, width_field=b'width_field', verbose_name='Upload a profile picture')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('cell_phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{8,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('minibio_br', models.TextField(max_length=500, verbose_name='Write a little about yourself in portuguese (public information)', blank=True)),
                ('minibio_en', models.TextField(max_length=500, verbose_name='Write a little about yourself in english (public information)', blank=True)),
                ('edu_complete', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('edu_exec_complete', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('edu_pm_complete', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('iwanttohelp', models.BooleanField(default=False, verbose_name='I want to help', choices=[(True, 'Yes'), (False, 'No')])),
                ('collaborator', models.BooleanField(default=True, choices=[(True, 'Yes'), (False, 'No')])),
                ('executive', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('project_manager', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('program_manager', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('general_coordinator', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
