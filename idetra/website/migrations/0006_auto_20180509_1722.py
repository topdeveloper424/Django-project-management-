# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20180509_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 17 digits allowed.")]),
        ),
    ]
