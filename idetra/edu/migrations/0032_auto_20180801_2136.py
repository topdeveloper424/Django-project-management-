# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0031_auto_20180730_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='course_chat_fk',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
