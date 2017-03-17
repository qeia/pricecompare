import re
import requests, urllib2
import json
app_id = 'yvivBJReHwD4dRg4xKA8NBDj'
url = 'http://www.bestbuy.com/site/pny-attache-4-16gb-usb-2-0-flash-drive-black/3789011.p?skuId=3789011'
p = re.compile('skuId=\d+')
item_id =  str(p.findall(url)[0])[6:]

print item_id
url = 'https://api.bestbuy.com/v1/products/'
url +=  item_id
url += '.json?'
url += 'show=regularPrice,onlineAvailability'
url += '&apiKey='+app_id
a =json.loads(urllib2.urlopen(url).read())
print a["regularPrice"],a["onlineAvailability"]
