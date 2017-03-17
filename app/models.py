from __future__ import unicode_literals

from django.db import models

class ItemModel(models.Model):
	item_id = models.CharField(max_length = 50, primary_key = True)
	ASIN = models.CharField(max_length=50)
	gamestopurl = models.CharField(max_length=200)
	walmartid = models.CharField(max_length = 50)
	ebayid = models.CharField(max_length=200)
	bestbuyurl = models.CharField(max_length = 200)
	
	amazon_available = models.BooleanField()
	walmart_available = models.BooleanField()
	gamestop_available = models.BooleanField()
	ebay_available = models.BooleanField()
	bestbuy_available = models.BooleanField()
	amazon_price = models.DecimalField(max_digits = 10, decimal_places = 5)	
	walmart_price = models.DecimalField(max_digits = 10, decimal_places = 5)
	gamestop_price = models.DecimalField(max_digits = 10, decimal_places = 5)
	ebay_price = models.DecimalField(max_digits = 10, decimal_places = 5)
	bestbuy_price = models.DecimalField(max_digits = 10, decimal_places = 5)
