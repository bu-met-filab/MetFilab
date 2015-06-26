from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class WorldbankCountry(models.Model):

	rowid = models.CharField(primary_key=True, max_length=40)
	code = models.CharField(max_length=5)
	long_name = models.CharField(max_length=100, blank=True, null=True)
	short_name = models.CharField(max_length=30, blank=True, null=True)
	wb2code = models.CharField(max_length=2, blank=True, null=True)
	income_group = models.CharField(max_length=50, blank=True, null=True)
	region = models.CharField(max_length=50, blank=True, null=True)
	lend_category = models.CharField(max_length=50, blank=True, null=True)
	other_group = models.CharField(max_length=50, blank=True, null=True)
	currency_unit = models.CharField(max_length=50, blank=True, null=True)


	def __str__(self):
		return '(' + self.code + ')-' + self.short_name

	class Meta:
		app_label = 'filab'
		db_table = 'worldbank_country'

