from django import forms

from threadedcomments.forms import ThreadedCommentForm

from .models import Course, Section, Lesson, Dictionary, Llink, Quizz, Question, UserCourse



class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
		'course_name',
		'course_name_br',
		'course_game_name',
		'course_game_name_br',
		'intro_video',
		'intro_video_br',
		'c_description', 
		'c_description_br', 
		'course_image',
		'main_edu',
		'token_file',
		'token_img',
		'exec_edu',
		'pm_edu',

	]

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = [
		'course_name_fk',
		'section_name',
		'section_name_br',
		'section_game_name',
		'section_game_name_br',
		's_description',
		's_description_br',


		]

class LessonForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = [
		'section_name_fk',
		'lesson_name',
		'lesson_name_br',
		'lesson_game_name',
		'lesson_game_name_br',
		'lesson_video',
		'lesson_video_br',
		'l_description',
		'l_description_br',
		'l_transcription',
		'l_transcription_br',

		]




class DictionaryForm(forms.ModelForm):
	class Meta:
		model = Dictionary
		fields = [
		'therm',
		'therm_br',
		'definition',
		'definition_br',


		]

class LlinkForm(forms.ModelForm):
	class Meta:
		model = Llink
		fields = [
		'llink_name_fk',
		'link_type',
		'link_name',
		'link_name_br',
		'link',
		'link_br',

		]

class QuizzForm(forms.ModelForm):
	class Meta:
		model = Quizz
		fields = [
		'lesson_name_fk',
		'quizz_name',
		'final_quizz',


		]



class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'quizz_name_fk',
			'question_name',
			'q_val_error',
			'q_val_error_br',
			'question',
			'question_br',
			'answer_1',
			'answer_1_br',
			'answer_1_correct',
			'answer_2',
			'answer_2_br',
			'answer_2_correct',
			'answer_3',
			'answer_3_br',
			'answer_3_correct',
			'answer_4',
			'answer_4_br',
			'answer_4_correct',
		]

QuestionInlineFormSet = forms.inlineformset_factory(
	Quizz, Question, form=QuestionForm, extra=0, min_num=1
) 


class UserCourseForm(forms.ModelForm):
	class Meta:
		model = UserCourse
		fields = [
			"user",
			"course",
			"finished"
			]









