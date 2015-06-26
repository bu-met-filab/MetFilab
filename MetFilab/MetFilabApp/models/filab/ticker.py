from django.db import models
from django.utils.translation import ugettext as _

class Ticker(models.Model):

	country = models.CharField(max_length=5, verbose_name=_("Country"))
	ticker = models.CharField(primary_key=True, max_length=10, verbose_name=_("Ticker"))
	ticker_name = models.CharField(max_length=100, verbose_name=_("Ticker Name"), blank=True, null=True)
	stock_exchange = models.CharField(max_length=20, verbose_name=_("Stock Exchange"), blank=True, null=True)

	def __str__(self):
		return '(' + self.ticker + ')-' + self.stock_exchange

	class Meta:
		app_label = 'filab'
		db_table = 'ticker'