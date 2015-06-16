from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from forms import SignInForm, SignUpForm, SignUpProfileFormSet
from MetFilabApp.models.app.profile import Profile

def signin(request):
	logout(request)
	if request.method == 'POST':
		form = SignInForm(data=request.POST)
		if form.is_valid():
			# login_user = authenticate(username=request.POST['username'],password=request.POST['password'])
			login_user = form.get_user()
			login(request, login_user)
			return redirect('/dashboard')
	else:
		form = SignInForm()
	return render(request, 'SignIn.html', {'form': form, 'isLoggedIn': 'False'})

@login_required
def signout(request):
	logout(request)
	return render(request, 'SignOut.html', {'isLoggedIn': 'False'})

def signup(request):
	user = User()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		formset = SignUpProfileFormSet(request.POST, instance=user)
		if form.is_valid():
			user = form.save(commit=False)

			formset = SignUpProfileFormSet(request.POST, instance=user)
			if formset.is_valid():
				form.save(commit=True)
				formset.save(commit=True)
				return render(request, 'SignUpFinish.html', {'isLoggedIn': 'False'})
	else:
		form = SignUpForm()
		formset = SignUpProfileFormSet(instance=user)

	return render(request, 'SignUp.html', {'form': form, 'formset': formset, 'isLoggedIn': 'False'})

