# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterField(
            model_name='section',
            name='course_name_fk',
            field=models.ForeignKey(related_name='sections', to='edu.Course'),
        ),
    ]
