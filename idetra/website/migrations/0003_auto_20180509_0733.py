# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180509_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
