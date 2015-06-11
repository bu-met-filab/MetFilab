from django.db import models

class ThomCurrency(models.Model):
	currency = models.CharField(max_length=5)
	currency_name = models.CharField(max_length=50)

	class Meta:
	app_lable = 'filab'
	db_table = 'thom_currency'
		