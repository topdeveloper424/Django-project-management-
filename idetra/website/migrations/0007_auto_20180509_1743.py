# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180509_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='iwanttohelp',
            field=models.BooleanField(default=False, verbose_name='I want to help'),
        ),
    ]
