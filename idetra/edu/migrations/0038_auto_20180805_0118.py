# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import edu.models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0037_userlesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='token_file',
            field=models.FileField(null=True, upload_to=edu.models.upload_location, blank=True),
        ),
    ]
