from django.db import models

class ThomCurrency(models.Model):
<<<<<<< HEAD
	
	currency = models.CharField(max_length=5)
	currency_name = models.CharField(max_length=50, blank=True)
=======
	currency = models.CharField(max_length=5, primary_key=True)
	currency_name = models.CharField(max_length=50)
>>>>>>> bu-met-filab/master

	def __str__(self):
		return '(' + self.currency + ')-' + self.currency_name

	class Meta:
		app_label = 'filab'
		db_table = 'thom_currency'
		