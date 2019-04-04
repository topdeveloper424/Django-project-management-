from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from website.models import User, Profile
from .models import Project, Team, WBS, Deliverable


User = get_user_model()


@login_required
def myarea(request):

	context = {


	}

	return render(request, "ci2_myarea.html", context)



@login_required
def project(request):

	context = {


	}

	return render(request, "ci3_project.html", context)



@login_required
def assets(request):

	context = {


	}

	return render(request, "ci4_assets.html", context)































# @login_required
# def ci(request, id=1):
	
# 	userp = request.user.profile
# 	p_project = Project.objects.all()

# 	proj = get_object_or_404(Project, id=id)
# 	try:
# 		x = p_project.get(id=request.POST[id])

# 	except (KeyError, Project.DoesNotExist):
# 		context = {
# 		"userp":userp,
# 		"p_project":p_project,
# 		"proj":proj,
# 		'error_message': "You didn't select a choice.",
# 		}
# 		return render(request, "ci.html", context)
# 	else:
# 		return HttpResponseRedirect(reverse('ci', args=(project.id,)))
# 	# if request.method == 'POST':
# 	# 	# proj = request.project.get(project_id=project_id),
# 	# 	proj = get_object_or_404(Project, id=id),

# 	context = {

# 	"userp":userp,
# 	"p_project":p_project,
# 	"proj":proj,

# 	}

# 	return render(request, "ci.html", context)
	