# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_name_fk', models.CharField(max_length=120, blank=True)),
                ('user_fk', models.CharField(max_length=120, blank=True)),
                ('comment_title', models.CharField(max_length=120, blank=True)),
                ('comment_text', models.TextField(max_length=1000, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=120, blank=True)),
                ('course_game_name', models.CharField(max_length=120, blank=True)),
                ('c_description', models.TextField(max_length=500, blank=True)),
                ('course_image', models.ImageField(upload_to=b'/courses/')),
                ('basic_links', models.TextField(max_length=500, blank=True)),
                ('advanced_links', models.TextField(max_length=500, blank=True)),
                ('final_quizz', models.CharField(max_length=120, blank=True)),
                ('token_file', models.CharField(max_length=120, blank=True)),
                ('sections_list', models.TextField(max_length=500, blank=True)),
                ('c_progress', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name_fk', models.CharField(max_length=120, blank=True)),
                ('lesson_name', models.CharField(max_length=120, blank=True)),
                ('lesson_video', models.CharField(max_length=120, blank=True)),
                ('lesson_game_name', models.CharField(max_length=120, blank=True)),
                ('l_description', models.TextField(max_length=500, blank=True)),
                ('l_transcription', models.TextField(max_length=100000, blank=True)),
                ('lesson_image', models.ImageField(upload_to=b'/lesson/')),
                ('quizz', models.TextField(max_length=500, blank=True)),
                ('l_progress', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quizz_name_fk', models.CharField(max_length=120, blank=True)),
                ('question_name', models.CharField(max_length=120, blank=True)),
                ('question', models.CharField(max_length=300, blank=True)),
                ('answer_1', models.CharField(max_length=300, blank=True)),
                ('answer_2', models.CharField(max_length=300, blank=True)),
                ('answer_3', models.CharField(max_length=300, blank=True)),
                ('answer_4', models.CharField(max_length=300, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_name_fk', models.CharField(max_length=120, blank=True)),
                ('quizz_name', models.CharField(max_length=120, blank=True)),
                ('final_quizz', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name_fk', models.CharField(max_length=120, blank=True)),
                ('section_name', models.CharField(max_length=120, blank=True)),
                ('section_game_name', models.CharField(max_length=120, blank=True)),
                ('s_description', models.TextField(max_length=500, blank=True)),
                ('section_image', models.ImageField(upload_to=b'/sections/')),
                ('lessons_list', models.TextField(max_length=500, blank=True)),
                ('s_progress', models.CharField(max_length=120, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
