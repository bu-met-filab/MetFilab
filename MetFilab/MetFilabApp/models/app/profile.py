from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Profile(models.Model):
	
	STATUS_APPLIED = 'A'
	STATUS_APPROVED = 'V'
	STATUS_REJECTED = 'R'

	STATUS_CHOICES = (
		(STATUS_APPLIED, _('Applied')),
		(STATUS_APPROVED, _('Approved')),
		(STATUS_REJECTED, _('Rejected')),
	)

	user = models.OneToOneField(User, primary_key=True)
	#Organization
	org = models.CharField(max_length=50)
	#Introduction
	intro = models.TextField(max_length=300)
	#Research Topic
	topic = models.CharField(max_length=100, blank=True, null=True)
	#Apply Reason
	reason = models.TextField(max_length=300)
	#Status
	status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=STATUS_APPLIED)
	#Reject Reason
	reject_reason = models.TextField(max_length=300, blank=True, null=True)

	class Meta:
		app_label = 'MetFilabApp'