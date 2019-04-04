# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0024_auto_20180623_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_1', models.BooleanField(default=False)),
                ('answer_2', models.BooleanField(default=False)),
                ('answer_3', models.BooleanField(default=False)),
                ('answer_4', models.BooleanField(default=False)),
                ('date_answered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_question_val', models.BooleanField(default=False)),
                ('date_answered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuizz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quizz_completed', models.BooleanField(default=False)),
                ('date_completed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_name_br',
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='quizz_name_br',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_1_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_2_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_3_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_4_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='q_val_error',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='q_val_error_br',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user_answer_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='user_answer_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='user_answer_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='user_answer_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userquizz',
            name='quizz_fk',
            field=models.ForeignKey(related_name='answered_quizes', to='edu.Quizz'),
        ),
        migrations.AddField(
            model_name='userquizz',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userquestion',
            name='question',
            field=models.ForeignKey(related_name='answered_questions', to='edu.Question'),
        ),
        migrations.AddField(
            model_name='userquestion',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userattempt',
            name='quiz',
            field=models.ForeignKey(related_name='attempts', to='edu.Quizz'),
        ),
        migrations.AddField(
            model_name='userattempt',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='question_fk',
            field=models.ForeignKey(related_name='answered_quetions', to='edu.Question'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
