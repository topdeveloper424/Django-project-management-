# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0011_auto_20180611_2351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': ' Courses'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name_plural': '  Sections'},
        ),
    ]
