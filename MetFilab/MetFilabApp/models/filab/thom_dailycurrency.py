from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext as _
from MetFilabApp.models.filab.thom_currency import ThomCurrency

class ThomDailyCurrency(models.Model):

	SOURCE_CHOICES = (
		('all','All',),
		('news','News',),
		('social','Social',),
		)

	rowid = models.CharField(primary_key=True)
	# currency = models.CharField(max_length=5)
	currency = models.ForeignKey(ThomCurrency,db_column='currency', verbose_name="Currency")
	date = models.DateField(verbose_name=_("Date"))
	time = models.TimeField(verbose_name=_("Time"))
	source = models.CharField(max_length=10, choices=SOURCE_CHOICES, verbose_name=_("Source"))
	buzz = models.FloatField(verbose_name=_("Buzz"))
	sentiment = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Sentiment"))
	optimism = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Optimism"))
	fear = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Fear"))
	joy = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Joy"))
	trust = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Trust"))
	violence = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Violence"))
	conflict = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Conflict"))
	urgency = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Urgency"))
	uncertainty = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Uncertainty"))
	price = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Price"))
	priceforecast = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Price Forecast"))
	carrytrade = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], verbose_name=_("Carry Trade"))
	currencypeginstability = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Currency Pegin Stability"))
	pricemomentum = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], verbose_name=_("Price Momentum"))

	class Meta:
		app_label = 'filab'
		db_table = 'thom_dailycurrency'
		
			