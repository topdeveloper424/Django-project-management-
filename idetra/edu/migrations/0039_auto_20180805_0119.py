# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import edu.models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0038_auto_20180805_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='token_img',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=edu.models.upload_location, blank=True),
        ),
    ]
