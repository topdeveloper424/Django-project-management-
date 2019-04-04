from django.utils.translation import ugettext as _
from django.utils import translation
from django.shortcuts import render, redirect
from .forms import ProfileForm, UserForm, IwForm
from edu.models import Dictionary
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.urlresolvers import resolve

User = get_user_model()

def home(request):

	user_language=''
	translation.activate(user_language)
	request.session[translation.LANGUAGE_SESSION_KEY] = user_language

	teamp = Profile.objects.filter(iwanttohelp=True)
	context = { 
	"teamp" : teamp,
	}
	return render(request, "home.html", context)

def profile(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			editform = UserForm(request.POST, instance=request.user)
			editformp = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
			iform = IwForm(request.POST, instance=request.user.profile)
			if editform.is_valid() and editformp.is_valid() and iform.is_valid():
				editform.save()
				editformp.save()
				iform.save()
			return redirect('/profile/')
		else:
			editform = UserForm(instance=request.user)
			editformp = ProfileForm(instance=request.user.profile)
			iform = IwForm(instance=request.user.profile)

		usershow = request.user
		userp = request.user.profile

		context = {
		"editform" : editform ,
		"editformp" : editformp ,
		"iform" : iform,
		"usershow": usershow ,
		"userp": userp ,
		}
	else:
		return redirect('/')
	return render(request, "profile.html", context)

def dictionary(request):
	dictionary = Dictionary.objects.all()
	context={"dictionary" : dictionary,}
	return render(request, "dictionary.html", context)



#-----------------------------------------------
# from .forms import CursosForm
# from .models import Cursos
	# def funcao(request):
# 	cursos = Cursos.objects.all(nao passo nada por aqui)
# 	cursos = Cursos.objects.get(passa um atributo da model aqui pra ele pegar 1)
# 	cursos = Cursos.objects.filter(passa um atributo da model aqui pra ele pegar lista)
# 	cursos.filter, etc
# 	videodocurso = Curso.video
# 	sections = Cursos.sections.all() #caso tenha related_name
# 	sections = Section.objects.filter(course=Cursos.objects.get()) # tem q ter os dois models rodando aqui dentro
# 	context = { "a" : a }
# 	return render(request, "pagina.html", context)
#-----------------------------------------------
#LANGUAGE_CODE = get_current_language
#-----------------------------------------------
# def base(request):
# 	if 'lang' in request.GET:
# 		translation.activate(request.GET.get('lang'))
	#title = _("Welcome!!!")
#-----------------------------------------------
	#{ "template key": view context}
#-----------------------------------------------
#external context
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	emailreply = instance.email
	# 	instance.save()
	# 	subject = _("Welcome!!!")
	# 	message = "testing" #"%s:%s via %s"% (emaill, nomee, 'IDETRA')
	# 	from_email = settings.EMAIL_HOST_USER
	# 	to_email = [emailreply]
	# 	send_mail(subject, message, from_email, to_email, fail_silently=False)
	# if request.user.is_authenticated():
	# 		title = _("Logged as %s") % (request.user)
			#context = {"title":"Thank you"}
#-----------------------------------------------

#WORKS!!!!

# @login_required
# @transaction.atomic
# def profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
        
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()

#         return redirect('/profile/')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)   

#     context = { 
#         "user_form" : user_form,
#         "profile_form" : profile_form,
#     }
#     return render(request, "profile.html", context)
