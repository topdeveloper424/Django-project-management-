# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci', '0002_auto_20180425_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='all_docs_folder',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date_plan',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date_real',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_progress',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='section_image',
            field=models.ImageField(null=True, upload_to=b'/projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_1',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_2',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_3',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_4',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_5',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_6',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_7',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tap_item_8',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
