from django.conf import settings
from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django_resized import ResizedImageField

BOOLEAN_YN = ((True, _(u'Yes')), (False, _(u'No')),)

def upload_location(instance, filename):
	return "%s/%s" % (instance.user, filename)

class Profile(models.Model):
	user 				= models.OneToOneField(settings.AUTH_USER_MODEL)
	name 				= models.CharField(_("Your Name"), max_length=120, null=True, blank=True)
	lastname 			= models.CharField(_("Your last name"), max_length=120, null=True, blank=True)
	middlenames 		= models.CharField(_("Your middle name(s)"), max_length=120, null=True, blank=True)
	picture 			= ResizedImageField(_("Upload a profile picture"),
							size=[150, 150], 
							crop=['middle', 'center'], 
							upload_to=upload_location,
							null=True,
	 						blank=True,
							)
	phone_regex 		= RegexValidator(regex=r'^\+?1?\d{8,15}$', message=_("Phone number must be entered in the format: '+999999999'. Up to 17 digits allowed."))
	cell_phone			= models.CharField(_("Use the format +999999999 - Up to 17 digits allowed."),validators=[phone_regex], max_length=17, null=True, blank=True)
	minibio_br 			= models.TextField(_("Write a little about yourself in portuguese (public information - 500 characters max)"), max_length=500, null=True, blank=True)
	minibio_en 			= models.TextField(_("Write a little about yourself in english (public information - 500 characters max)"), max_length=500, null=True, blank=True)
	edu_complete 		= models.BooleanField(_("Edu Complete"), default=False, choices=BOOLEAN_YN)
	edu_exec_complete	= models.BooleanField(_("Edu Exec Complete"), default=False, choices=BOOLEAN_YN)
	edu_pm_complete		= models.BooleanField(_("Edu PM Complete"), default=False, choices=BOOLEAN_YN)
	iwanttohelp			= models.BooleanField(_("I want to help"), default=False, choices=BOOLEAN_YN)
	collaborator		= models.BooleanField(_("Collaborator"), default=True, choices=BOOLEAN_YN)
	executive			= models.BooleanField(_("Executive"), default=False, choices=BOOLEAN_YN)
	project_manager		= models.BooleanField(_("Project Manager"), default=False, choices=BOOLEAN_YN)
	program_manager		= models.BooleanField(_("Program Manager"), default=False, choices=BOOLEAN_YN)
	general_coordinator	= models.BooleanField(_("General Coordinator"), default=False, choices=BOOLEAN_YN)
	timestamp 			= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated 			= models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_text(self.user.username)
		#return str(self.user.username) #in case of error, use: str(self.xxx) instead of self.xxx

	def set_edu_module_as_complete(self, module_type):
		from edu.models import Course

		if module_type == Course.MAIN:
			self.edu_complete = True
		elif module_type == Course.EXEC:
			self.edu_exec_complete = True
		else:
			self.edu_pm_complete = True
		self.save()


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
		try:
			Profile.objects.create(user=instance)
		except:
			pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


