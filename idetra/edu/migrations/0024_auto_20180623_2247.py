# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0023_auto_20180621_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='lessons_list',
        ),
        migrations.RemoveField(
            model_name='section',
            name='lessons_list_br',
        ),
        migrations.RemoveField(
            model_name='section',
            name='s_progress',
        ),
    ]
