# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0030_usercourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='token_img',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='token_file',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
