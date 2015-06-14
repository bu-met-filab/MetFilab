from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ThomDailyCurrency(models.Model):

	SOURCE_CHOICES = (
		('all','All',),
		('news','News',),
		('social','Social',),
		)

	rowid = models.CharField(primary_key=True, max_length=40)
	currency = models.CharField(max_length=5)
	date = models.DateField()
	time = models.TimeField()
	source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
	buzz = models.FloatField(blank=True, null=True)
	sentiment = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	optimism = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	fear = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], blank=True, null=True)
	joy = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], blank=True, null=True)
	trust = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	violence = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], blank=True, null=True)
	conflict = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	urgency = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	uncertainty = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], blank=True, null=True)
	price = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	priceforecast = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	carrytrade = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], blank=True, null=True)
	currencypeginstability = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)
	pricemomentum = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(-1)], blank=True, null=True)

	class Meta:
		app_lable = 'filab'
		db_table = 'thom_dailycurrency'
		
			