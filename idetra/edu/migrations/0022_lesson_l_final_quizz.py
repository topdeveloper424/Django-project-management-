# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0021_auto_20180620_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='l_final_quizz',
            field=models.BooleanField(default=False),
        ),
    ]
