# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0027_auto_20180630_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquestion',
            name='user_question_val',
        ),
    ]
