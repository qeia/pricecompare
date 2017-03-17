from selenium import webdriver
from bs4 import BeautifulSoup
import requests, urllib2,json
import re
import bottlenose
ACCESS_KEY_AMAZON ='AKIAJGA5VXGOC5CACFVQ'
SECRET_KEY_AMAZON ='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'
A_ID = 'dertr-20'
ACCESS_KEY_WALMART= 'gum7sbth2pn6v2ck24hfsk7w'
EBAY_APP_ID = 'Benjamin-products-PRD-92466ad44-13674f29'
BESTBUY_API_KEY = 'yvivBJReHwD4dRg4xKA8NBDj'


class ItemLookup:
	def walmart(self,ITEM_ID):
		ACCESS_KEY = 'gum7sbth2pn6v2ck24hfsk7w'
		url = 'http://api.walmartlabs.com/v1/items/{}?apiKey={}&format=json'.format(ITEM_ID,ACCESS_KEY)
		response = urllib2.urlopen(url)
		response = json.load(response)
		available = False
		price = response['salePrice']
		if response['stock']=="Available":
			available = True
		return float(price),available	

	
	def gamestop(self,url):
		headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
		source_code = requests.get(url,headers=headers).text
		soup = BeautifulSoup(source_code,"lxml")
		found1 = soup.find_all('h3', class_="ats-prodBuy-price")
		found2 = soup.find_all('a', class_='ats-prodBuy-notAvail')
		price = 0
		available = False
		if len(found1)>0:			
			st = found1[0]
			st = str(st)
			price = st[47:][:-12]		
			price =  float(price)	
		else:
			print "NOT FOUND"
		if len(found2)==1:
			available = False
		else:
			available = True
		return price, available
	def amazon(self,ITEM_ID):
		ACCESS_KEY_AMAZON = 'AKIAJGA5VXGOC5CACFVQ'
		SECRET_KEY_AMAZON = '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'
		A_ID = 'dertr-20'

		amazon = bottlenose.Amazon(ACCESS_KEY_AMAZON,SECRET_KEY_AMAZON,A_ID)
		price = 0
		available = False
		response = amazon.ItemLookup(ItemId=ITEM_ID,ResponseGroup='OfferSummary')
		soup = BeautifulSoup(response,'xml')
		a = soup.find_all('FormattedPrice')
		b = soup.find_all('TotalNew')[0]
		p = re.compile('\$[\d.,]+')
		q = re.compile('[\d.,]+')
		if len(a) > 0:
			for x in a:
				if len (p.findall(str(x)))>0:
					price = p.findall(str(x))
		number = q.findall(str(b))
		price = price[0]
		price = float(price[1:])
		if int(number[0]) > 0:
			available = True
		return price , available
	def ebay(self,url):
		p = re.compile('/\d\d\d\d\d\d\d\d\d\d+')
		available = True
		price = 0
		
		item_id =  str(p.findall(url)[0])[1:]
		url = 'http://open.api.ebay.com/shopping?callname=GetSingleItem&itemId='
		url +=  item_id
		url += '&responseencoding=JSON'
		url += '&appid=' + EBAY_APP_ID
		url += '&version=515'
		a =json.loads(urllib2.urlopen(url).read())
		print urllib2.urlopen(url).read()
		price = float(a["Item"]["ConvertedCurrentPrice"]["Value"])
		return price, available
	def bestbuy(self,url):
		p = re.compile('skuId=\d+')
		item_id =  str(p.findall(url)[0])[6:]
		url = 'https://api.bestbuy.com/v1/products/'
		url +=  item_id
		url += '.json?'
		url += 'show=regularPrice,onlineAvailability'
		url += '&apiKey='+BESTBUY_API_KEY
		a =json.loads(urllib2.urlopen(url).read())
		return float(a["regularPrice"]),a["onlineAvailability"]		
		
			
				
				
		