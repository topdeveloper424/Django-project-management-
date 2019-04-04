# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0009_auto_20180611_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='advanced_links',
        ),
        migrations.RemoveField(
            model_name='course',
            name='advanced_links_br',
        ),
        migrations.RemoveField(
            model_name='course',
            name='basic_links',
        ),
        migrations.RemoveField(
            model_name='course',
            name='basic_links_br',
        ),
        migrations.AddField(
            model_name='lesson',
            name='advanced_links',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='advanced_links_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='basic_links',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='basic_links_br',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
