# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='alert_timeframe',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='t_duration',
            field=models.IntegerField(blank=True),
        ),
    ]
