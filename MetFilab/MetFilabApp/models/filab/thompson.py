from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

class ThomCurrency(models.Model):
	currency = models.CharField(max_length=5, primary_key=True, verbose_name=_("Currency"))
	currency_name = models.CharField(max_length=50, verbose_name=_("Currency Name"))

	def __str__(self):
		return '(' + self.currency + ')-' + self.currency_name

	class Meta:
		app_label = 'filab'
		db_table = 'thom_currency'

class ThomDailyCurrency(models.Model):

	SOURCE_CHOICES = (
		('all','All',),
		('news','News',),
		('social','Social',),
		)

	currency = models.ForeignKey(ThomCurrency,db_column='currency', verbose_name="Currency")
	date = models.DateField(verbose_name=_("Date"))
	time = models.TimeField(verbose_name=_("Time"))
	source = models.CharField(max_length=10, choices=SOURCE_CHOICES, verbose_name=_("Source"))
	buzz = models.FloatField(verbose_name=_("Buzz"), blank=True, null=True)
	sentiment = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Sentiment"), blank=True, null=True)
	optimism = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Optimism"), blank=True, null=True)
	fear = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Fear"), blank=True, null=True)
	joy = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Joy"), blank=True, null=True)
	trust = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Trust"), blank=True, null=True)
	violence = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Violence"), blank=True, null=True)
	conflict = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Conflict"), blank=True, null=True)
	urgency = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Urgency"), blank=True, null=True)
	uncertainty = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Uncertainty"), blank=True, null=True)
	price = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Price"), blank=True, null=True)
	priceforecast = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Price Forecast"), blank=True, null=True)
	carrytrade = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Carry Trade"), blank=True, null=True)
	currencypeginstability = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Currency Pegin Stability"), blank=True, null=True)
	pricemomentum = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Price Momentum"), blank=True, null=True)

	class Meta:
		app_label = 'filab'
		db_table = 'thom_dailycurrency'
