# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0010_auto_20180611_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Llink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('basic_link_name', models.CharField(max_length=120, blank=True)),
                ('basic_link_name_br', models.CharField(max_length=120, blank=True)),
                ('basic_link', models.CharField(max_length=120, blank=True)),
                ('basic_link_br', models.CharField(max_length=120, blank=True)),
                ('adv_link_name', models.CharField(max_length=120, blank=True)),
                ('adv_link_name_br', models.CharField(max_length=120, blank=True)),
                ('adv_link', models.CharField(max_length=120, blank=True)),
                ('adv_link_br', models.CharField(max_length=120, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Clinks',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sections_list_br',
        ),
        migrations.RemoveField(
            model_name='section',
            name='section_image',
        ),
        migrations.AddField(
            model_name='section',
            name='lessons_list_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='s_description_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='section_game_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='section_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
    ]
