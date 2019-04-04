# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20180509_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Use the format +999999999 - Up to 17 digits allowed.', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 17 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='collaborator',
            field=models.BooleanField(default=True, verbose_name='Collaborator', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='edu_complete',
            field=models.BooleanField(default=False, verbose_name='Edu Complete', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='edu_exec_complete',
            field=models.BooleanField(default=False, verbose_name='Edu Exec Complete', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='edu_pm_complete',
            field=models.BooleanField(default=False, verbose_name='Edu PM Complete', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='executive',
            field=models.BooleanField(default=False, verbose_name='Executive', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='general_coordinator',
            field=models.BooleanField(default=False, verbose_name='General Coordinator', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='minibio_br',
            field=models.TextField(max_length=500, null=True, verbose_name='Write a little about yourself in portuguese (public information - 500 characters max)', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='minibio_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Write a little about yourself in english (public information - 500 characters max)', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='program_manager',
            field=models.BooleanField(default=False, verbose_name='Program Manager', choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='project_manager',
            field=models.BooleanField(default=False, verbose_name='Project Manager', choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
