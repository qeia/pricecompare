from django_cron import CronJobBase, Schedule
from .models import ItemModel
from itemlookup import ItemLookup




class CronJob(CronJobBase):
	print 'running cron'
	RUN_EVERY_MINS = 120
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'my_app.my_cron_job'  
	i=ItemLookup()
	items = ItemModel.objects.all()
	print items
	for item in items:
		print 'x',item
		print item.item_id
		#print i.amazon(item.ASIN)

		try:
			amazon = i.amazon(item.ASIN)
			print amazon
			item.amazon_available = amazon[1] #Boolean field, True if the product is in stock
			item.amazon_price = amazon[0] 
		except Exception as err:
			print err,"amazon"
		try:		
			walmart = i.walmart(item.walmartid)
			item.walmart_available = walmart[1]
			item.walmart_price = walmart[0]
		except Exception as err:
			print err,"walmart"
		try:		
			gamestop = i.gamestop(item.gamestopurl)
			item.gamestop_available = gamestop[1]
			item.gamestop_price = gamestop[0]

		except Exception as err:
			print err,"gamestop"	
		try:		
			ebay = i.ebay(item.ebayid)
			item.ebay_available = ebay[1]
			item.ebay_price = ebay[0]
			
		except Exception as err:
			print err,"ebay"
		try:
			print item.bestbuyurl		
			bestbuy = i.bestbuy(item.bestbuyurl)
			item.bestbuy_available = bestbuy[1]
			item.bestbuy_price = bestbuy[0]
			
		except Exception as err:
			print err,"bestbuy"		
		try:	
			item.save()
		except Exception as err:
			print err	

		
		print item
		print 'saved'



        
