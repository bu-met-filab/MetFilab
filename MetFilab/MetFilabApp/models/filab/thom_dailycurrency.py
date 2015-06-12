from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from MetFilabApp.models.filab.thom_currency import ThomCurrency

class ThomDailyCurrency(models.Model):

	SOURCE_CHOICES = (
		('all','All',),
		('news','News',),
		('social','Social',),
		)

	rowid = models.CharField(primary_key=True)
	# currency = models.CharField(max_length=5)
	currency = models.ForeignKey(ThomCurrency,db_column='currency')
	date = models.DateField()
	time = models.TimeField()
	source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
	buzz = models.FloatField()
	sentiment = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	optimism = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	fear = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
	joy = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
	trust = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	violence = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
	conflict = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	urgency = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	uncertainty = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
	price = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	priceforecast = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	carrytrade = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
	currencypeginstability = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])
	pricemomentum = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)])

	class Meta:
		app_label = 'filab'
		db_table = 'thom_dailycurrency'
		
			