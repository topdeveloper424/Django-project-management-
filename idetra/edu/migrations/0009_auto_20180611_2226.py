# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0008_auto_20180607_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='advanced_links_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='basic_links_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='c_description_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_game_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='final_quizz_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='sections_list_br',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
