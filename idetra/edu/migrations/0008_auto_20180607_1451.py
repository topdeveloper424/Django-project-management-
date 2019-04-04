# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0007_dictionary'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='definition_br',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='therm_br',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
