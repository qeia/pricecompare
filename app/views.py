from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ItemInfo
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, urllib2,json
import re
import bottlenose
from .models import ItemModel
from itemlookup import ItemLookup
i = ItemLookup()
# Create your views here.
def ShowPrice(request):
	form = ItemInfo(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			print request.POST
			asin = request.POST.get("asin","")
			gamestopurl = request.POST.get("gamestopurl","")
			walmartid = request.POST.get("walmartid","")
			ebayurl = request.POST.get("ebayurl","")
			bestbuyurl = request.POST.get("bestbuyurl","")
			amazon =i.amazon(asin)
			gamestop =i.gamestop(gamestopurl)
			walmart = i.walmart(walmartid)
			ebay = i.ebay(ebayurl)
			bestbuy = i.bestbuy(bestbuyurl)
			
			

			return HttpResponse("amazon "+str(amazon[0])+str(amazon[1])+"\ngamestop "+str(gamestop[0])+str(gamestop[1])+
				"\nwalmart "+str(walmart[0])+str(walmart[1])+ " \nebay "+str(ebay[0])+str(ebay[1]) + "\nbestbuy" + str(bestbuy[0])+ str(bestbuy[1]))
	return HttpResponse('Nothing Now, go to /form/')		

def	ShowForm(request):
	form1 = ItemInfo
	return render(request,'app/form.html',{'form':form1})

def main(request):
	items = ItemModel.objects.all()
	print "SFA:AFAFIFAJAIFJIAFJIAJIFJAFI"
	new_item = []
	amazon =[]
	ebay = {}
	walmart = {}
	bestbuy = {}
	gamestop = {}
	for item in items:
		dic = {}
		dic['id']=item.item_id
		dic['amazon_available'] = item.amazon_available
		dic['amazon_price'] = item.amazon_price
		dic['walmart_available'] = item.walmart_available
		dic['walmart_price'] = item.walmart_price
		dic['gamestop_available'] = item.gamestop_available
		dic['gamestop_price'] = item.gamestop_price
		dic['ebay_available'] = item.ebay_available
		dic['ebay_price'] = item.ebay_price
		dic['bestbuy_available'] = item.bestbuy_available
		dic['bestbuy_price'] = item.bestbuy_price
		new_item.append(dic)		
	return render(request,'app/main.html',{'items':new_item})	

















         