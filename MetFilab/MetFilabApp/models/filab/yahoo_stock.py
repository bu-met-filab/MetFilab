from django.db import models

class YahooStock(models.Model):
	
	rowid = models.CharField(primary_key=True, max_length=40)
	symbol = models.CharField(max_length=10)
	exchange_symbol = models.CharField(max_length=10)
	date = models.DateField()
	open_price = models.FloatField(blank=True, null=True)
	high_price = models.FloatField(blank=True, null=True)
	low_price = models.FloatField(blank=True, null=True)
	close_price = models.FloatField(blank=True, null=True)
	volume = models.IntegerField(blank=True, null=True)
	adj_close = models.FloatField(blank=True, null=True)

	class Meta:
		app_lable = 'filab'
		db_table = 'yahoo_stock'