from django.db import models
from django.utils.translation import ugettext as _

class ThomCurrency(models.Model):
	currency = models.CharField(max_length=5, primary_key=True, verbose_name=_("Currency"))
	currency_name = models.CharField(max_length=50, verbose_name=_("Currency Name"))

	def __str__(self):
		return '(' + self.currency + ')-' + self.currency_name

	class Meta:
		app_label = 'filab'
		db_table = 'thom_currency'
		