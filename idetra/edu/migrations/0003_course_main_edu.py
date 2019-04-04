# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_auto_20180509_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='main_edu',
            field=models.BooleanField(default=False),
        ),
    ]
