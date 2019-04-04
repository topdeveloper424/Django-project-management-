# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0016_auto_20180613_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(populate_from=[b'course_name'], editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='slug_br',
            field=django_extensions.db.fields.AutoSlugField(populate_from=[b'course_name_br'], editable=False, blank=True),
        ),
    ]
