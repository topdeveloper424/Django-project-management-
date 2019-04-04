# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0014_auto_20180612_0211'),
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
            ],
            options={
                'verbose_name_plural': ' Chats',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '        Courses'},
        ),
        migrations.AlterModelOptions(
            name='dictionary',
            options={'verbose_name_plural': '  Dictionary'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name_plural': '      Lessons'},
        ),
        migrations.AlterModelOptions(
            name='llink',
            options={'verbose_name': 'Link', 'verbose_name_plural': '     Links'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': '   Questions'},
        ),
        migrations.AlterModelOptions(
            name='quizz',
            options={'verbose_name_plural': '    Quizzes'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name_plural': '       Sections'},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_image',
        ),
        migrations.AddField(
            model_name='dictionary',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 3, 16, 26, 972552, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dictionary',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 3, 16, 39, 158353, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='l_description_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='l_transcription_br',
            field=models.TextField(max_length=100000, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_game_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_name_br',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='quizz_br',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='section_name_fk',
            field=models.ForeignKey(related_name='lessons', to='edu.Section'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='lesson_name_fk',
            field=models.ForeignKey(related_name='lesson_quizz', to='edu.Lesson'),
        ),
        migrations.AddField(
            model_name='chat',
            name='course_chat_fk',
            field=models.ForeignKey(related_name='chat', to='edu.Lesson'),
        ),
    ]
