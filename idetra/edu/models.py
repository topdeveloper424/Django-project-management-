import datetime 

from django.conf import settings
from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.db.models import CharField, Case, Value, When, F

def upload_location(instance, filename):
	return "%s/%s" % (instance.course_name, filename)

class Course(models.Model):
	MAIN = 0
	EXEC = 1
	PM = 2

	course_name 		= models.CharField(max_length=120, blank=True)
	slug 				= AutoSlugField(populate_from=['course_name'], overwrite=True)
	course_name_br 		= models.CharField(max_length=120, blank=True)
	slug_br				= AutoSlugField(populate_from=['course_name_br'], overwrite=True)
	course_game_name	= models.CharField(max_length=120, blank=True)
	course_game_name_br	= models.CharField(max_length=120, blank=True)
	intro_video			= models.CharField(max_length=120, blank=True, null=True)
	intro_video_br		= models.CharField(max_length=120, blank=True, null=True)
	c_description		= models.TextField(max_length=500, blank=True)
	c_description_br	= models.TextField(max_length=500, blank=True)
	course_image		= models.ImageField(upload_to=upload_location, height_field="height_field", width_field="width_field", null=True, blank=True)
	height_field		= models.IntegerField(default=0, null=True, blank=True)
	width_field			= models.IntegerField(default=0, null=True, blank=True)
	token_file			= models.FileField(upload_to=upload_location,blank=True, null=True)
	token_img	  		= models.ImageField(upload_to=upload_location, height_field="height_field", width_field="width_field", null=True, blank=True)
	main_edu			= models.BooleanField(default=False)
	exec_edu			= models.BooleanField(default=False)
	pm_edu				= models.BooleanField(default=False)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "        Courses"

	def __unicode__(self):
		return smart_text(self.course_name)

	def get_quizes(self):
		return Quizz.objects.filter(lesson_name_fk__section_name_fk__course_name_fk=self)

	def get_questions(self):
		"""Returns all questions belonging to the course"""
		return Question.objects.filter(quizz_name_fk__lesson_name_fk__section_name_fk__course_name_fk=self)

	def get_course_percentage_progress(self, user):
		""""
		Calculates the percentage of progress of conclusion
		of the user for a given course based on the amount
		of completed quizes 
		"""
		number_of_quizes = self.get_quizes().count()
		number_of_completed_quizes = self.get_completed_quizes_by(user).count()

		if number_of_quizes > 0:
			percentage = (float(number_of_completed_quizes) / float(number_of_quizes)) * 100
			return int(percentage)
			#return round(percentage, 2)
		else:
			return 0



	def verify_and_update_course_status(self, user):
		"""
		Check if user finished all quizes
		and changes status to TRUE
		if all quizes were concluded
		"""
		number_of_quizes = self.get_quizes().count()

		if self.get_completed_quizes_by(user).count() == number_of_quizes:
			user_course, __ = UserCourse.objects.get_or_create(user=user, course=self)
			user_course.finished = True
			user_course.save()


	def get_completed_quizes_by(self, user):
		return UserQuiz.objects.filter(
			user=user, quiz__lesson_name_fk__section_name_fk__course_name_fk=self, finished=True
		)

	def has_token(self):
		return False if self.token_img == "" or None else True 

	def get_module_types(self):
		types = []
		if self.main_edu:
			types.append(self.MAIN)
		if self.exec_edu:
			types.append(self.EXEC)
		if self.pm_edu:
			types.append(self.PM)
		
		return types


	def get_module_type(self):
		if self.main_edu:
			return self.MAIN
		elif self.exec_edu:
			return self.EXEC
		else:
			return self.PM

	def get_module_query(self):
		query = dict()
		if self.main_edu:
			query.update({"main_edu": True})
		if self.exec_edu:
			query.update({"exec_edu": True})
		if self.pm_edu:
			query.update({"pm_edu": True})

		return query 

class Section(models.Model):
	course_name_fk		= models.ForeignKey("Course", related_name="sections") #FK
	section_name		= models.CharField(max_length=120, blank=True)
	section_name_br		= models.CharField(max_length=120, blank=True)
	section_game_name	= models.CharField(max_length=120, blank=True)
	section_game_name_br= models.CharField(max_length=120, blank=True)
	s_description		= models.TextField(max_length=500, blank=True)
	s_description_br	= models.TextField(max_length=500, blank=True)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "       Sections"

	def __unicode__(self):
		return smart_text(self.section_name)

class Lesson(models.Model):
	section_name_fk		= models.ForeignKey("Section", related_name="lessons") #FK
	lesson_name			= models.CharField(max_length=120, blank=True)
	slug 				= AutoSlugField(populate_from=['lesson_name'], overwrite=True)
	lesson_name_br		= models.CharField(max_length=120, blank=True)
	slug_br				= AutoSlugField(populate_from=['lesson_name_br'], overwrite=True)
	lesson_game_name	= models.CharField(max_length=120, blank=True)
	lesson_game_name_br	= models.CharField(max_length=120, blank=True)
	lesson_video		= models.CharField(max_length=120, blank=True)
	lesson_video_br		= models.CharField(max_length=120, blank=True)
	l_description		= models.TextField(max_length=500, blank=True)
	l_description_br	= models.TextField(max_length=500, blank=True)
	l_transcription		= models.TextField(max_length=100000, blank=True)
	l_transcription_br	= models.TextField(max_length=100000, blank=True)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "      Lessons"

	def __unicode__(self):
		return smart_text(self.lesson_name)

# ----------------------------------- OVERALL VALIDATION START

class UserQuiz(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='terminated_quizes', on_delete=models.CASCADE)
	quiz = models.ForeignKey('Quizz', related_name='+', on_delete=models.CASCADE)
	finished = models.BooleanField(default=False)

	def __unicode__(self):
		return smart_text(self.user)

class UserLesson(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lessons', on_delete=models.CASCADE)
	lesson = models.ForeignKey(Lesson, related_name='+', on_delete=models.CASCADE)
	finished = models.BooleanField(default=False)

	def __unicode__(self):
		return smart_text(self.user)

class UserCourse(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses', on_delete=models.CASCADE)
	course = models.ForeignKey('Course', related_name='students', on_delete=models.CASCADE)
	finished = models.BooleanField(default=False) 
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return smart_text(self.user)

# ----------------------------------- OVERALL VALIDATION END
# ----------------------------------- QUIZES START

class Quizz(models.Model):
	lesson_name_fk		= models.OneToOneField("Lesson", related_name="lesson_quizz") #FK
	quizz_name			= models.CharField(max_length=120, blank=True)#TALVEZ NAO
	final_quizz			= models.BooleanField(default=False)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "    Quizzes"

	def __unicode__(self):
		return smart_text(self.quizz_name)

class Question(models.Model):
	quizz_name_fk		= models.ForeignKey("Quizz", related_name="quizz_questions") #FK
	question_name		= models.CharField(max_length=120, blank=True)
	q_val_error			= models.CharField(max_length=500, blank=True, null=True)
	q_val_error_br 		= models.CharField(max_length=500, blank=True, null=True)
	question 			= models.CharField(max_length=300, blank=True)
	question_br			= models.CharField(max_length=300, blank=True)
	answer_1 			= models.CharField(max_length=300, blank=True)
	answer_1_br			= models.CharField(max_length=300, blank=True)
	answer_1_correct 	= models.BooleanField(default=False)
	user_answer_1 		= models.BooleanField(default=False)
	answer_2 			= models.CharField(max_length=300, blank=True)
	answer_2_br			= models.CharField(max_length=300, blank=True)
	answer_2_correct	= models.BooleanField(default=False)
	user_answer_2 		= models.BooleanField(default=False)
	answer_3 			= models.CharField(max_length=300, blank=True)
	answer_3_br			= models.CharField(max_length=300, blank=True)
	answer_3_correct 	= models.BooleanField(default=False)
	user_answer_3 		= models.BooleanField(default=False)
	answer_4 			= models.CharField(max_length=300, blank=True)
	answer_4_br			= models.CharField(max_length=300, blank=True)
	answer_4_correct  	= models.BooleanField(default=False)
	user_answer_4 		= models.BooleanField(default=False)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "   Questions"

	def __unicode__(self):
		return smart_text(self.question_name)

	def is_correct(self, answer_number):
		return getattr(self, 'answer_{number}_correct'.format(number=answer_number)) 

	def get_answers_in_english(self):
		return (self.answer_1, self.answer_2, self.answer_3, self.answer_4)

	def get_answers_in_portuguese(self):
		return (self.answer_1_br, self.answer_2_br, self.answer_3_br, self.answer_4_br)

	
class UserQuestion(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answered_questions')
	question = models.ForeignKey('Question')
	date_answered = models.DateTimeField(auto_now_add=True)	
	
# ---------------- QUIZ ATTEMPTS VALIDATION START

MAX_ATTEMPTS_BY_DAY = 3

def validate_attempts_by_day(user, quiz):
	"""VALIDATES NUMBER OF ATTEMPTS, BY USER, PER DAY"""
	today = datetime.datetime.today()
	number_of_attempts = user.attempts.filter(
		quiz=quiz,
		created_at__range=(
			datetime.datetime.combine(today, datetime.time.min),
			datetime.datetime.combine(today, datetime.time.max)
		)
	).count() 

	return number_of_attempts < MAX_ATTEMPTS_BY_DAY, number_of_attempts


class UserAttempt(models.Model):
	"""STORES NUMBER OF ATTEMPTS OF A QUIZ BY THE USER"""
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, related_name='attempts', on_delete=models.CASCADE
	)
	quiz = models.ForeignKey('Quizz', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

# ---------------- QUIZ ATTEMPTS VALIDATION END

# ----------------------------------- QUIZES END

BASIC = "Basic"
ADVANCED = "Advanced"
link_types = ((BASIC, "Basic"),(ADVANCED, "Advanced"))


class Llink(models.Model):
	llink_name_fk		= models.ForeignKey("Lesson", related_name="lesson_links", null=True) #FK
	link_type 			= models.CharField(max_length=10, choices=link_types, blank=True, null=True)
	link_name 			= models.CharField(max_length=120, blank=True)
	link_name_br 		= models.CharField(max_length=120, blank=True)
	link 				= models.CharField(max_length=120, blank=True)
	link_br 			= models.CharField(max_length=120, blank=True)
	
	class Meta:
		verbose_name = "Link"
		verbose_name_plural = "     Links"

	def __unicode__(self):
		return smart_text(self.link_name)

class Dictionary(models.Model):
	therm 				= models.CharField(max_length=120, blank=True, null=True)
	therm_br 			= models.CharField(max_length=120, blank=True, null=True)
	definition 			= models.TextField(max_length=500, blank=True, null=True)
	definition_br 		= models.TextField(max_length=500, blank=True, null=True)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "  Dictionary"

	def __unicode__(self):
		return smart_text(self.therm)
