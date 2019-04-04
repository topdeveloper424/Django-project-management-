# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0025_auto_20180625_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('b_title', models.CharField(max_length=120, null=True, blank=True)),
                ('b_text', models.TextField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
