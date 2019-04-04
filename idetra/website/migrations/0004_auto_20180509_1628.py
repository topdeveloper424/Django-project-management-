# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20180509_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=django_resized.forms.ResizedImageField(force_format=None, quality=0, upload_to=website.models.upload_location, crop=[b'middle', b'center'], keep_meta=True, blank=True, null=True, verbose_name='Upload a profile picture', size=[150, 150]),
        ),
    ]
