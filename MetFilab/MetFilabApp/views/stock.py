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

@login_required
def search(request):
	countryform = ChooseCountryForm()
	if request.method == 'POST':
		form = SearchStockForm(request.POST, country=country)
		#if form.is_valid():
		#else:
		# 	return HttpResponse(form.non_field_errors)
	else:
		form = SearchStockForm()
	return render(request, 'Stock.html', {'searchform': form, 'countryform':countryform, 'actionUrl': '/stock/search'})
