# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import edu.models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0005_auto_20180531_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='height_field',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='width_field',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=edu.models.upload_location, blank=True),
        ),
    ]
