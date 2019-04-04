# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0020_auto_20180618_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='intro_video',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='intro_video_br',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
