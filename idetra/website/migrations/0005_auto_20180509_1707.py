# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180509_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='profile',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{8,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=120, null=True, verbose_name='Your last name', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middlenames',
            field=models.CharField(max_length=120, null=True, verbose_name='Your middle name(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='minibio_br',
            field=models.TextField(max_length=500, null=True, verbose_name='Write a little about yourself in portuguese (public information)', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='minibio_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Write a little about yourself in english (public information)', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=120, null=True, verbose_name='Your Name', blank=True),
        ),
    ]
