from django.contrib import admin
from .models import Profile
from .forms import AdminForm

class ProfileAdmin(admin.ModelAdmin):
	list_display = [
	"__unicode__",
	'name', 
	'lastname',
	'iwanttohelp', 
	'edu_complete',
	'edu_exec_complete', 
	'edu_pm_complete',
	'collaborator',
	'executive',
	'project_manager',
	'program_manager',
	'general_coordinator',
	'timestamp',
	'updated',
	]
	form = AdminForm
	#lists what to appear on admin users list

	class Meta:
		model = Profile

admin.site.register(Profile, ProfileAdmin)



#basic admin

# from django.contrib import admin
# from .models import Profile
# admin.site.register(Prodile)