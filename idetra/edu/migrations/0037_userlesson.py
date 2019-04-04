# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0036_auto_20180805_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(related_name='+', to='edu.Lesson')),
                ('user', models.ForeignKey(related_name='lessons', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
