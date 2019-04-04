from django import forms
from .models import Project, Team


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = [
		'project_name',
		'gp_name',
		'tap_item_1',
		'tap_item_2',
		'tap_item_3',
		'tap_item_4',
		'tap_item_5',
		'tap_item_6',
		'tap_item_7',
		'tap_item_8',
		'all_docs_folder',
		'start_date',
		'end_date_plan',
		'end_date_real',
		'p_progress',

		]

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = [
		'team_name',


		]
