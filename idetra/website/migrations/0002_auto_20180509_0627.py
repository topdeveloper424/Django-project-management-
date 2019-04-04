# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to=website.models.upload_location, width_field=b'width_field', height_field=b'height_field', blank=True, null=True, verbose_name='Upload a profile picture'),
        ),
    ]
