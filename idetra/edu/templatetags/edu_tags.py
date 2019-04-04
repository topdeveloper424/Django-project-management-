from django.db.models import Case, Value, When, BooleanField
from django import template
from edu.models import Course
from django.db.models import Q

register = template.Library()


@register.inclusion_tag('question_error.html', takes_context=True)
def question_error(context, question, language='en'):
    has_error = question.id in context['errors']
    return {
        'has_error': has_error,
        'question': question,
        'language': language
    }

@register.simple_tag
def course_progress(user, course):
	return course.get_course_percentage_progress(user) 


@register.simple_tag
def overall_progress(user):
    courses = Course.objects.filter(main_edu=True)
    progress = sum([c.get_course_percentage_progress(user) for c in courses]) 

    return int(progress / courses.count())


@register.simple_tag
def overall_executive_progress(user):
    courses = Course.objects.filter(exec_edu=True)
    progress = sum([c.get_course_percentage_progress(user) for c in courses]) 

    return int(progress / courses.count())


@register.simple_tag
def overall_pm_progress(user):
    courses = Course.objects.filter(pm_edu=True)
    progress = sum([c.get_course_percentage_progress(user) for c in courses]) 
    
    return int(progress / courses.count()) 
 

@register.inclusion_tag("user_courses.html")
def user_courses(user):
    finished_courses = user.courses.filter(finished=True).values_list('course__pk', flat=True)
    courses = Course.objects.annotate(
        finished=Case(
            When(id__in=finished_courses, then=True),
            default=False,
            output_field=BooleanField()
        )
    )
    return {"courses": courses}
