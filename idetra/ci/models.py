from django.conf import settings
from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.db.models.signals import post_save
from django.dispatch import receiver

class Project(models.Model):
	project_name 		= models.CharField(max_length=120, blank=True, null=True)
	gp_name				= models.CharField(max_length=120, blank=True) #this might be dinamic....
	section_image		= models.ImageField(upload_to='/projects/', height_field=None, width_field=None, null=True)
	tap_item_1			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_2			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_3			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_4			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_5			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_6			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_7			= models.TextField(max_length=500, blank=True, null=True)
	tap_item_8			= models.TextField(max_length=500, blank=True, null=True)
	all_docs_folder		= models.CharField(max_length=120, blank=True, null=True)
	start_date 			= models.DateField(blank=True, null=True)
	end_date_plan		= models.DateField(blank=True, null=True)
	end_date_real		= models.DateField(blank=True, null=True)
	p_progress 			= models.CharField(max_length=120, blank=True, null=True) #this might be dinamic....
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.project_name)

class Team(models.Model):
	project_name_fk		= models.CharField(max_length=120, blank=True) #FK
	user_fk				= models.CharField(max_length=120, blank=True) #FK
	team_name 			= models.CharField(max_length=120, blank=True)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.team_name)

class WBS(models.Model):
	project_name_fk		= models.CharField(max_length=120, blank=True) #FK
	wbs_name 			= models.CharField(max_length=120, blank=True)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.wbs_name)

class Deliverable(models.Model):
	wbs_fk				= models.CharField(max_length=120, blank=True) #FK
	deliverable_name	= models.CharField(max_length=120, blank=True)
	d_info				= models.TextField(max_length=1000, blank=True)
	d_predecessor		= models.CharField(max_length=120, blank=True) #Intra-recursive
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.deliverable_name)

class Task(models.Model):
	deliverable_name_fk	= models.CharField(max_length=120, blank=True) #FK
	task_name			= models.CharField(max_length=120, blank=True)
	t_info				= models.TextField(max_length=1000, blank=True)
	t_duration 			= models.IntegerField(blank=True)
	t_cost 				= models.DecimalField(max_digits=9, decimal_places=2)
	t_predecessor		= models.CharField(max_length=120, blank=True) #Intra-recursive. can have multiple predecessors
	t_responsible		= models.CharField(max_length=120, blank=True) #users from team list - required (executes)
	t_accountable		= models.CharField(max_length=120, blank=True) #users from team list - required (only 1)
	t_consulted			= models.CharField(max_length=120, blank=True) #users from team list
	t_informed			= models.CharField(max_length=120, blank=True) #users from team list
	delivered			= models.BooleanField(default=False)
	delivery_link		= models.CharField(max_length=500, blank=True)
	alert 				= models.BooleanField(default=False) #alert on email?
	alert_timeframe 	= models.IntegerField(blank=True) #alert x days before task
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.task_name)


# seria interessante poder usar a do edu ou o mesmo estilo do edu, ja que as pessoas vao estar acostumadas

class ProjectChat(models.Model):
	project_name_fk		= models.CharField(max_length=120, blank=True) #FK
	user_fk				= models.CharField(max_length=120, blank=True) #FK
	task_fk				= models.CharField(max_length=120, blank=True) #FK
	pc_comment_title	= models.CharField(max_length=120, blank=True)
	pc_comment_text		= models.TextField(max_length=1000, blank=True)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.pc_comment_title)









