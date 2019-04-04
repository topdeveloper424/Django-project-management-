# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0028_remove_userquestion_user_question_val'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(related_name='+', to='edu.Quizz')),
                ('user', models.ForeignKey(related_name='terminated_quizes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question_fk',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userquizz',
            name='quizz_fk',
        ),
        migrations.RemoveField(
            model_name='userquizz',
            name='user',
        ),
        migrations.AlterField(
            model_name='userattempt',
            name='quiz',
            field=models.ForeignKey(to='edu.Quizz'),
        ),
        migrations.AlterField(
            model_name='userattempt',
            name='user',
            field=models.ForeignKey(related_name='attempts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userquestion',
            name='question',
            field=models.ForeignKey(to='edu.Question'),
        ),
        migrations.AlterField(
            model_name='userquestion',
            name='user',
            field=models.ForeignKey(related_name='answered_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
        migrations.DeleteModel(
            name='UserQuizz',
        ),
    ]
