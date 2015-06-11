from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import DateFormat, TimeFormat
from MetFilabApp.views.forms import SearchCurrencyForm
from MetFilabApp.models.filab.thom_dailycurrency import ThomDailyCurrency

@login_required
def search(request):
	if request.method == 'POST':
		form = SearchCurrencyForm(request.POST)
		if form.is_valid():
			currency = form.cleaned_data['currency']
			source = form.cleaned_data['sentiment_source']
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']

			result = ThomDailyCurrency.objects
						.filter(currency=currency, source=source, date__gte=start_date, date__lte=end_date)
						.order_by('date')

			dict_result = {}
			data = []
			for r in result:
				dict_r = {}
				dict_r['name'] = r.date
				dict_r['x'] = DateFormat(r.date).format('U')
				dict_r['y'] = r.sentiment

				data.append(dict_r)

			dict_result['data_chart'] = data
			dict_result['data_table'] = result.values()

			return JsonResponse(dict_result)
		else:
			return HttpResponse('')
	else:
		form = SearchCurrencyForm()
	return render(request, 'Currency.html', {'form': form, 'actionUrl': '/currency/search'})
