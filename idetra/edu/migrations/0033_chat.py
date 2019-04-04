# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0032_auto_20180801_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=120, null=True, blank=True)),
                ('chat_text', models.TextField(max_length=500, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course_chat_fk', models.ForeignKey(related_name='chat', to='edu.Lesson')),
            ],
            options={
                'verbose_name_plural': ' Chats',
            },
        ),
    ]
