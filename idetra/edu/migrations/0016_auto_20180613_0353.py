# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0015_auto_20180613_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='advanced_links',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='advanced_links_br',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='basic_links',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='basic_links_br',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='quizz',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='quizz_br',
        ),
        migrations.AddField(
            model_name='llink',
            name='llink_name_fk',
            field=models.ForeignKey(related_name='lesson_links', to='edu.Lesson', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_1_br',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_2_br',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_3_br',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_4_br',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_br',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='quizz',
            name='quizz_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='quizz_name_fk',
            field=models.ForeignKey(related_name='quizz_questions', to='edu.Quizz'),
        ),
    ]
