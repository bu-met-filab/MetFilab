from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def home_page(request):
	if request.user.is_authenticated():
		return redirect('/dashboard')
	return render(request, 'Home.html')

@login_required
def dash_board(request):
	return render(request, 'DashBoard.html')
