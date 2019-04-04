# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0017_auto_20180618_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_video_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='userlesson',
            name='lesson',
            field=models.ForeignKey(related_name='+', to='edu.Lesson'),
        ),
        migrations.AddField(
            model_name='userlesson',
            name='user',
            field=models.ForeignKey(related_name='lessons', to=settings.AUTH_USER_MODEL),
        ),
    ]
