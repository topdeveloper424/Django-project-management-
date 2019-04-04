# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0019_auto_20180618_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'course_name'], blank=True, overwrite=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug_br',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'course_name_br'], blank=True, overwrite=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'lesson_name'], blank=True, overwrite=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug_br',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=[b'lesson_name_br'], blank=True, overwrite=True),
        ),
    ]
