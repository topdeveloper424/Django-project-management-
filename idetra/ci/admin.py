from django.contrib import admin
from .forms import ProjectForm, TeamForm
from .models import Project, Team



class CIAdmin(admin.ModelAdmin):
	
	form = ProjectForm


	class Meta:
		model = Project
admin.site.register(Project, CIAdmin)