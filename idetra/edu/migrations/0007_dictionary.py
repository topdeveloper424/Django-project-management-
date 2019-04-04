# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0006_auto_20180531_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('therm', models.CharField(max_length=120, null=True, blank=True)),
                ('definition', models.TextField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
