from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
from django.contrib import auth as authlib
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from MetFilabApp.models.app.profile import Profile

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
		fields = '__all__'
		widgets = {'intro': Textarea(attrs={'cols': 60, 'rows': 5}),
				   'topic': Textarea(attrs={'cols': 60, 'rows': 2}),
				   'reason': Textarea(attrs={'cols': 60, 'rows': 5}),
				   'reject_reason': Textarea(attrs={'cols': 60, 'rows': 5}),}

SignUpProfileFormSet = inlineformset_factory(User, Profile, form=ProfileForm, can_delete=False, max_num=1, extra=1, exclude=('reject_reason',))

class SignInForm(AuthenticationForm):
	"""docstring for SignInForm"""
	def __init__(self, *args, **kwargs):
		super(SignInForm, self).__init__(*args, **kwargs)
		for name, field in self.fields.items():
			if field.widget.attrs.has_key('class'):
				field.widget.attrs['class'] += 'form-control'
			else:
				field.widget.attrs.update({'class':'form-control'})
