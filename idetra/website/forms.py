from django import forms
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		'picture',
		'name', 
		'middlenames', 
		'lastname', 
		'cell_phone', 
		'minibio_en', 
		'minibio_br', 
		]

class IwForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		'iwanttohelp', 
		]


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
		'username', 
		'email', 
		]

class AdminForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		'user', 
		'name', 
		'lastname', 
		'middlenames', 
		'picture',
		# "height_field",
		# "width_field",
		'cell_phone', 
		'minibio_en', 
		'minibio_br', 
		'edu_complete',
		'edu_exec_complete', 
		'edu_pm_complete',
		'iwanttohelp',
		'collaborator',
		'executive',
		'project_manager',
		'program_manager',
		'general_coordinator',
		]











