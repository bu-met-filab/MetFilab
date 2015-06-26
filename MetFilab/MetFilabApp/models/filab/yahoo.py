from django.db import models
from django.utils.translation import ugettext as _

class YahooStock(models.Model):
	
	rowid = models.CharField(primary_key=True, max_length=40)
	symbol = models.CharField(max_length=10, verbose_name=_("Symbol"))
	exchange_symbol = models.CharField(max_length=10, verbose_name=_("Exchange Symbol"))
	date = models.DateField(verbose_name=_("Data"))
	open_price = models.FloatField(verbose_name=_("Open Price"), blank=True, null=True)
	high_price = models.FloatField(verbose_name=_("High Price"), blank=True, null=True)
	low_price = models.FloatField(verbose_name=_("Low Price"), blank=True, null=True)
	close_price = models.FloatField(verbose_name=_("Close Price"), blank=True, null=True)
	volume = models.IntegerField(verbose_name=_("Volume"), blank=True, null=True)
	adj_close = models.FloatField(verbose_name=_("Adj Close"), blank=True, null=True)

	def __str__(self):
		return '(' + self.symbol + ')-' + self.exchange_symbol
		
	class Meta:
		app_label = 'filab'
		db_table = 'yahoo_stock'