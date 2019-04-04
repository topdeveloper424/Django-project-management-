from django.contrib import admin
from .forms import CourseForm, LessonForm, DictionaryForm, LlinkForm, QuizzForm, QuestionForm, SectionForm, UserCourseForm
from .models import Course, Section, Lesson, Dictionary, Llink, Quizz, Question, UserCourse

class EduAdmin(admin.ModelAdmin):
	form = CourseForm
	class Meta:
		model = Course
admin.site.register(Course, EduAdmin)

class SectionAdmin(admin.ModelAdmin):
	form = SectionForm
	class Meta:
		model = Section
admin.site.register(Section, SectionAdmin)

class LessonAdmin(admin.ModelAdmin):
	form = LessonForm
	class Meta:
		model = Lesson
admin.site.register(Lesson, LessonAdmin)

class DictionaryAdmin(admin.ModelAdmin):
	form = DictionaryForm
	class Meta:
		model = Lesson
admin.site.register(Dictionary, DictionaryAdmin)

class LlinkAdmin(admin.ModelAdmin):
	form = LlinkForm
	class Meta:
		model = Llink
admin.site.register(Llink, LlinkAdmin)

class QuizzAdmin(admin.ModelAdmin):
	form = QuizzForm
	class Meta:
		model = Quizz
admin.site.register(Quizz, QuizzAdmin)

class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	class Meta:
		model = Question
admin.site.register(Question, QuestionAdmin)

class UserCourseAdmin(admin.ModelAdmin):	 
	form = UserCourseForm
	class Meta:
		model = UserCourse
admin.site.register(UserCourse, UserCourseAdmin)





