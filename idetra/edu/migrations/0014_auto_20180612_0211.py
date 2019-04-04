# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0013_auto_20180612_0210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '   Courses'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name_plural': ' Lessons'},
        ),
    ]
