from django import forms
from django.db import models
from django.forms.models import inlineformset_factory, modelformset_factory
from django.utils.translation import ugettext as _
from django.contrib import auth as authlib
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from MetFilabApp.models.app.profile import Profile
from MetFilabApp.models.filab.thom_currency import ThomCurrency
from MetFilabApp.models.filab.thom_dailycurrency import ThomDailyCurrency


class SignUpForm(UserCreationForm):
	"""docstring for SignUpForm"""
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += 'form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})

	class Meta:
		model = authlib.get_user_model()
		fields = ('first_name','last_name','email','username','password1','password2')

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.is_active = False
		if commit:
			user.save()
		return user

class ProfileForm(forms.ModelForm):

	def __init__(self, *args, ** kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += ' form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Profile
		fields = ('__all__')
		widgets = {'intro': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
				   'topic': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
				   'reason': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
				   'reject_reason': forms.Textarea(attrs={'cols': 100, 'rows': 3}),}
		labels = {
            "org": _("Organization"),
            "intro": _("Self Introduction"),
            "topic": _("Research Topic"),
            "reason": _("Reason of Application"),
            "reject_reason": _("Reason of Rejections"),
        }

SignUpProfileFormSet = inlineformset_factory(User, Profile, form=ProfileForm, can_delete=False, max_num=1, extra=1, exclude=('user','status','reject_reason',))

class SignInForm(AuthenticationForm):
	"""docstring for SignInForm"""
	def __init__(self, *args, **kwargs):
		super(SignInForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += 'form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})

class SearchCurrencyForm(forms.Form):

	currency = forms.ModelChoiceField(queryset=ThomCurrency.objects.all())
	sentiment_source = forms.ChoiceField(choices=ThomDailyCurrency.SOURCE_CHOICES)
	start_date = forms.DateField()
	end_date = forms.DateField()
	drawable_columns = forms.MultipleChoiceField()

	def __init__(self, *args, **kwargs):
		super(SearchCurrencyForm, self).__init__(*args, **kwargs)
		coltuples = []
		for f in ThomDailyCurrency._meta.get_fields():
			if type(f) == models.FloatField:
				coltuples += [(f.name, f.verbose_name)]
		self.fields['drawable_columns'] = forms.MultipleChoiceField(choices=coltuples)

		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += ' form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})

	def clean_end_date(self):
		startdate = self.cleaned_data['start_date']
		enddate = self.cleaned_data['end_date']
		if enddate < startdate:
			raise forms.ValidationError(_(
				'Iteration end date should be later than it\'s start date !'))
		
		return enddate

	class Meta:
		labels = {
			"currency": _("Currency"),
			"sentiment_source": _("Source"),
			"start_date": _("Start Date"),
			"end_date": _("End Date"),
			"drawable_columns": _("Drawable Columns"),
		}
