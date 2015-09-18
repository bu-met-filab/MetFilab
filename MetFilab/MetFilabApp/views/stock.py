from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils.dateformat import DateFormat
from MetFilabApp.utils.DateTimeDjangoJSONEncoder import DateTimeDjangoJSONEncoder
from MetFilabApp.views.forms import SearchCurrencyForm, SearchStockForm, ChooseCountryForm
from MetFilabApp.models.filab.thompson import ThomDailyCurrency
from MetFilabApp.models.filab.yahoo import YahooStock
from MetFilabApp.models.filab.worldbank import WorldbankCountry
from MetFilabApp.models.filab.ticker import Ticker

@login_required
def search(request):
	
	countryform = ChooseCountryForm()

	if request.method == 'POST':
		countryform = ChooseCountryForm(request.POST)
		# pField = request.POST
		# selCountry = pField.get('country','')
		if countryform.is_valid():
			searchform = SearchStockForm(country=countryform.cleaned_data['country'].code)
			
		#form = SearchStockForm(country=request.POST.get('country'))
		#searchform = SearchStockForm(country=countryform.cleaned_data['country'])
		# searchform = SearchStockForm(country=selCountry)
		#if Searchform.is_valid():
		#else:
		# 	return HttpResponse(form.non_field_errors)
	else:
		searchform = SearchStockForm()

	return render(request, 'Stock.html', {'searchform': searchform, 'countryform':countryform, 'actionUrl': '/stock/search'})

def querysymbol(request):
	if request.method == 'POST':
		countryform = ChooseCountryForm(request.POST)
		result=Ticker.objects.filter(country=countryform.cleaned_data['country']).exclude(ticker_name=None)
		dict_result = {};


        


