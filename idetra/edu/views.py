from django.utils.translation import ugettext as _
from django.utils import translation
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.db import transaction
from django.core.urlresolvers import resolve
from django.db.models import Q
from django.http import JsonResponse
from django.db.models import BooleanField, Case, Value, When

from django_comments.models import Comment

from .forms import CourseForm, QuestionInlineFormSet
from .models import (Course, Section, Lesson, Quizz, 
					 Question, Dictionary, User,
					 UserQuestion, UserQuiz, UserCourse)


User = get_user_model()


@login_required
def edu(request):
	dictionary = Dictionary.objects.all()
	course = Course.objects.all()
	educourses = Course.objects.filter(main_edu=True)
	extracourses = Course.objects.filter(main_edu=False)
	tpic = Lesson.objects.all()
	usershow = request.user
	userp = request.user.profile

	context = {
		"dictionary" : dictionary ,
		"course" : course ,
		"extracourses" : extracourses ,
		"educourses" : educourses ,
		"tpic" : tpic ,
		"usershow" : usershow ,
		"userp" : userp,
	}

	return render(request, "edu.html", context)

@login_required
def course(request, slug):
	course = Course.objects.all()
	dictionary = Dictionary.objects.all()
	c_course = get_object_or_404(Course, Q(slug_br=slug) | Q(slug=slug))
	pb = '75%'
	sections = c_course.sections.prefetch_related('lessons')

	context = {
		"c_course": c_course ,
		"course": course ,
		"pb": pb,
		"dictionary": dictionary,
		"sections": sections
	}
	return render(request, "course.html", context)


@login_required
def lesson(request, slug_course, slug_lesson):

	course = Course.objects.all()
	dictionary = Dictionary.objects.all()
	c_course = get_object_or_404(Course, Q(slug_br=slug_course) | Q(slug=slug_course))
	c_lesson = get_object_or_404(Lesson, Q(slug_br=slug_lesson) | Q(slug=slug_lesson))

	completed, module_type = verify_user_module_status(user=request.user, from_course=c_course)
	if completed:
		request.user.profile.set_edu_module_as_complete(module_type)

	lessons = c_course.sections.prefetch_related('lessons')
	sections = c_course.sections.prefetch_related('lessons')

	# usuario comecou a assistir a licao
	user_lesson, __ = request.user.lessons.get_or_create(lesson=c_lesson)

	from .models import validate_attempts_by_day, UserAttempt, MAX_ATTEMPTS_BY_DAY

	__, tries = validate_attempts_by_day(request.user, c_lesson.lesson_quizz)

	errors = []
	user_quiz, __ = UserQuiz.objects.get_or_create(user=request.user, quiz=c_lesson.lesson_quizz) 
	course_percentage = c_course.get_course_percentage_progress(user=request.user)
	
	if request.method == 'POST':
		if tries < MAX_ATTEMPTS_BY_DAY:
			# Guarda tentativa de resposta
			UserAttempt.objects.create(quiz=c_lesson.lesson_quizz, user=request.user)

			answers = request.POST.copy()
			# Remove csrf token da requisicao
			del answers['csrfmiddlewaretoken']  

			number_of_correct_answers = 0
			for question_id, answer in answers.items():
				question = get_object_or_404(Question, pk=question_id)
				if question.is_correct(answer):
					UserQuestion.objects.get_or_create(user=request.user, question=question)
					number_of_correct_answers += 1
				else:
					errors.append(question.id)
		# Atualiza valor do numero de tentativas quando um POST for realizado
		__, tries = validate_attempts_by_day(request.user, c_lesson.lesson_quizz)

		# Indica que o quiz foi terminado apos responder corretamente todas as perguntas 		
		if number_of_correct_answers == c_lesson.lesson_quizz.quizz_questions.count():
			# Cria entrada para indicar que usuario comecou a fazer o curso
			UserCourse.objects.get_or_create(user=request.user, course=c_course)
			user_quiz, __ = UserQuiz.objects.update_or_create(
				user=request.user, quiz=c_lesson.lesson_quizz, defaults={'finished': True}
			) 

			course_percentage = c_course.get_course_percentage_progress(user=request.user)

	c_course.verify_and_update_course_status(user=request.user)

	user_courses = get_user_courses(user=request.user)

	context = {
		"c_course": c_course ,
		"course": course ,
		"dictionary": dictionary,
		"lessons": lessons ,
		"c_lesson": c_lesson ,
		"sections" : sections,
		"watched": user_lesson.finished ,
		"errors": errors,
		"tries": tries,
		"quizz_correct": user_quiz.finished,
		"course_percentage": course_percentage,
		"user_courses": user_courses

	}
	return render(request, "lesson.html", context)


@csrf_protect
def message(request, id):
    context = {
        'message': get_object_or_404(Message, pk=id),
    }
    return render(request, 'core/message.html', context)


@login_required
def update_lesson_progress(request, lesson_id):
	data = {}
	if request.is_ajax():
		lesson = request.user.lessons.get(lesson_id=lesson_id)
		lesson.finished = True # nao seria False aqui?
		lesson.save()
		data['ok'] = True
	else:
		data['ok'] = False

	return JsonResponse(data)


def dictionary(request):
	dictionary = Dictionary.objects.all()
	context={"dictionary" : dictionary,}
	return render(request, "dictionary.html", context)


def is_author(user, comment):
	"""Verifica se o usuario eh autor do comentario"""
	return comment.user == user 


@login_required
def delete_comment(request, pk):
	comment = get_object_or_404(Comment, pk=pk, user=request.user)
	comment.delete()

	return JsonResponse({'ok': True})


def get_user_courses(user):
	finished_courses = user.courses.filter(finished=True).values_list('pk', flat=True)
	return Course.objects.annotate(
		finished=Case(
			When(pk__in=finished_courses, then=Value(True)),
			default=Value(False),
			output_field=BooleanField()
		)
	)


def verify_user_module_status(user, from_course):
	for type in from_course.get_module_types():
		if module_is_finished(user, type):
			return (True, type)

	return (False, None)


def module_is_finished(user, type):
	if type == Course.MAIN:
		query = {"main_edu": True}
	elif type == Course.EXEC:
		query = {"exec_edu": True}
	else:
		query = {"pm_edu": True}

	courses = Course.objects.filter(**query)
	progress = sum([c.get_course_percentage_progress(user) for c in courses]) 	

	return int(progress / courses.count()) == 100
