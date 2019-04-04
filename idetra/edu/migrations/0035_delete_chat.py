# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0034_remove_chat_course_chat_fk'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
