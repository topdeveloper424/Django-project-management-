# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0022_lesson_l_final_quizz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='llink',
            old_name='adv_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='llink',
            old_name='adv_link_br',
            new_name='link_br',
        ),
        migrations.RenameField(
            model_name='llink',
            old_name='adv_link_name',
            new_name='link_name',
        ),
        migrations.RenameField(
            model_name='llink',
            old_name='adv_link_name_br',
            new_name='link_name_br',
        ),
        migrations.RemoveField(
            model_name='llink',
            name='basic_link',
        ),
        migrations.RemoveField(
            model_name='llink',
            name='basic_link_br',
        ),
        migrations.RemoveField(
            model_name='llink',
            name='basic_link_name',
        ),
        migrations.RemoveField(
            model_name='llink',
            name='basic_link_name_br',
        ),
        migrations.AddField(
            model_name='llink',
            name='link_type',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'Basic', b'Basic'), (b'Advanced', b'Advanced')]),
        ),
    ]
