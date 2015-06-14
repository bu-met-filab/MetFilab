from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	
	STATUS_APPLIED = 'A'
	STATUS_APPROVED = 'V'
	STATUS_REJECTED = 'R'

	STATUS_CHOICES = (
		(STATUS_APPLIED, 'Applied'),
		(STATUS_APPROVED, 'Approved'),
		(STATUS_REJECTED, 'Rejected'),
	)

	user = models.OneToOneField(User)
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