# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0026_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='lesson_name_fk',
            field=models.OneToOneField(related_name='lesson_quizz', to='edu.Lesson'),
        ),
    ]
