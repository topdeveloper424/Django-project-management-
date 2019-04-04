# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0035_delete_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlesson',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='userlesson',
            name='user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='c_progress',
        ),
        migrations.RemoveField(
            model_name='course',
            name='final_quizz',
        ),
        migrations.RemoveField(
            model_name='course',
            name='final_quizz_br',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sections_list',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='l_final_quizz',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='l_progress',
        ),
        migrations.DeleteModel(
            name='UserLesson',
        ),
    ]
