from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils.dateformat import DateFormat
from MetFilabApp.utils.DateTimeDjangoJSONEncoder import DateTimeDjangoJSONEncoder
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

			result = ThomDailyCurrency.objects.filter(currency=currency,
													  source=source, 
													  date__gte=start_date, 
													  date__lte=end_date
													 ).order_by('date')

			dict_result = {}
			data = []
			table_row = []
			table_col = []
			for r in result:
				dict_r = {}
				dict_r['name'] = r.date
				dict_r['x'] = int(DateFormat(r.date).format('U')) * 1000
				dict_r['y'] = r.sentiment
				dict_r['color'] = 'red'
				data.append(dict_r)

				dict_t = {}
				dict_t['currency'] = r.currency.currency
				dict_t['date'] = r.date
				dict_t['time'] = r.time
				dict_t['source'] = r.source
				dict_t['buzz'] = r.buzz
				dict_t['sentiment'] = r.sentiment
				dict_t['optimism'] = r.optimism
				dict_t['fear'] = r.fear
				dict_t['joy'] = r.joy
				dict_t['trust'] = r.trust
				dict_t['violence'] = r.violence
				dict_t['conflict'] = r.conflict
				dict_t['urgency'] = r.urgency
				dict_t['uncertainty'] = r.uncertainty
				dict_t['price'] = r.price
				dict_t['priceforecast'] = r.priceforecast
				dict_t['carrytrade'] = r.carrytrade
				dict_t['currencypeginstability'] = r.currencypeginstability
				dict_t['pricemomentum'] = r.pricemomentum
				table_row.append(dict_t)


			for f in result[0]._meta.get_fields():
				dict_c = {}
				dict_c['field'] = f.name
				dict_c['title'] = f.verbose_name
				table_col.append(dict_c)

			dict_result['data_chart'] = data
			dict_result['data_table'] = {'data_column': table_col, 'data_row': table_row}

			return JsonResponse(dict_result)
		# else:
		# 	return HttpResponse(form.non_field_errors)
	else:
		form = SearchCurrencyForm()
	return render(request, 'Currency.html', {'form': form, 'actionUrl': '/currency/search'})
