# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wbs_fk', models.CharField(max_length=120, blank=True)),
                ('deliverable_name', models.CharField(max_length=120, blank=True)),
                ('d_info', models.TextField(max_length=1000, blank=True)),
                ('d_predecessor', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=120, blank=True)),
                ('gp_name', models.CharField(max_length=120, blank=True)),
                ('section_image', models.ImageField(upload_to=b'/projects/')),
                ('tap_item_1', models.TextField(max_length=500, blank=True)),
                ('tap_item_2', models.TextField(max_length=500, blank=True)),
                ('tap_item_3', models.TextField(max_length=500, blank=True)),
                ('tap_item_4', models.TextField(max_length=500, blank=True)),
                ('tap_item_5', models.TextField(max_length=500, blank=True)),
                ('tap_item_6', models.TextField(max_length=500, blank=True)),
                ('tap_item_7', models.TextField(max_length=500, blank=True)),
                ('tap_item_8', models.TextField(max_length=500, blank=True)),
                ('all_docs_folder', models.CharField(max_length=120, blank=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date_plan', models.DateField(blank=True)),
                ('end_date_real', models.DateField(blank=True)),
                ('p_progress', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectChat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name_fk', models.CharField(max_length=120, blank=True)),
                ('user_fk', models.CharField(max_length=120, blank=True)),
                ('task_fk', models.CharField(max_length=120, blank=True)),
                ('pc_comment_title', models.CharField(max_length=120, blank=True)),
                ('pc_comment_text', models.TextField(max_length=1000, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deliverable_name_fk', models.CharField(max_length=120, blank=True)),
                ('task_name', models.CharField(max_length=120, blank=True)),
                ('t_info', models.TextField(max_length=1000, blank=True)),
                ('t_duration', models.IntegerField(max_length=3, blank=True)),
                ('t_cost', models.DecimalField(max_digits=9, decimal_places=2)),
                ('t_predecessor', models.CharField(max_length=120, blank=True)),
                ('t_responsible', models.CharField(max_length=120, blank=True)),
                ('t_accountable', models.CharField(max_length=120, blank=True)),
                ('t_consulted', models.CharField(max_length=120, blank=True)),
                ('t_informed', models.CharField(max_length=120, blank=True)),
                ('delivered', models.BooleanField(default=False)),
                ('delivery_link', models.CharField(max_length=500, blank=True)),
                ('alert', models.BooleanField(default=False)),
                ('alert_timeframe', models.IntegerField(max_length=3, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name_fk', models.CharField(max_length=120, blank=True)),
                ('user_fk', models.CharField(max_length=120, blank=True)),
                ('team_name', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WBS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name_fk', models.CharField(max_length=120, blank=True)),
                ('wbs_name', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
