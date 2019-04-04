# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_course_main_edu'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exec_edu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='pm_edu',
            field=models.BooleanField(default=False),
        ),
    ]
