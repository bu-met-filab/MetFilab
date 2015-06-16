from django.db import models
from MetFilab.MetFilabApp.models.filab.worldbank import WorldbankCountry

class AlexEquity(models.Model):

	rowid = models.CharField(primary_key=True, max_length=40)
	newsid = models.CharField(db_column='newsID',max_length=50)
	timestamp = models.DateTimeField()
	ticker = models.CharField(max_length=15)
	country = models.ForeignKey(WorldbankCountry, to_field='code')
	date = models.DateField()
	time = models.TimeField()
	sentiment = models.IntegerField()
	confidence = models.FloatField()
	novelty = models.IntegerField()
	subjects = models.CharField(max_length=100)
	relevance = models.FloatField()

	class Meta:
		abstract = True
		app_lable = 'filab'


class AlexEquity1999(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_1999'


class AlexEquity2000(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2000'


class AlexEquity2001(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2001'


class AlexEquity2002(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2002'


class AlexEquity2003(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2003'


class AlexEquity2004(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2004'


class AlexEquity2005(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2005'


class AlexEquity2006(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2006'


class AlexEquity2007(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2007'


class AlexEquity2008(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2008'


class AlexEquity2009(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2009'


class AlexEquity2010(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2010'


class AlexEquity2011(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2011'


class AlexEquity2012(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2012'


class AlexEquity2013(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2013'


class AlexEquity2014(AlexEquity):

	class Meta(AlexEquity.Meta):
		db_table = 'alex_equity_2014'