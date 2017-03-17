import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricecompare.settings")
django.setup()
from django.contrib.auth.models import ItemLookup

if __name__ == '__main__':
	print 'running cron'
	i=ItemLookup()
	items = ItemModel.objects.all()
	for item in items:
		try:
			amazon = i.ItemLookup(item.ASIN)
			item.amazon_available = amazon[1] #Boolean field, True if the product is in stock
			item.amazon_price = amazon[0] 
		except Exception as err:
			print err
		try:		
			walmart = i.ItemLookup(item.walmartid)
			item.walmart_available = walmart[1]
			item.walmart_price = walmart[0]
		except Exception as err:
			print err
		try:		
			gamestop = i.ItemLookip(item.gamestopurl)
			item.gamestop_available = gamestop[1]
			item.gamestop_price = gamestop[0]

		except Exception as err:
			print err	
		try:		
			ebayid = i.ItemLookip(item.ebayurl)
			item.ebay_available = ebay[1]
			item.ebay_price = ebay[0]
			
		except Exception as err:
			print err
		try:		
			bestbuy = i.ItemLookip(item.bestbuyurl)
			item.bestbuy_available = ebay[1]
			item.bestbuy_price = ebay[0]
			
		except Exception as err:
			print err		
		try:	
			item.save()
		except Exception as err:
			print err	

		
		print item
		print 'saved'