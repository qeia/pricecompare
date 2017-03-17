import re
import requests, urllib2
import json
app_id = 'Benjamin-products-PRD-92466ad44-13674f29'
url = 'http://www.ebay.com/itm/Sony-PlayStation-4-Slim-500GB-Console-Jet-Black-PS4-NEW-2016-/262800155662?hash=item3d301c240e:g:I3IAAOSwEzxYXYuj'
p = re.compile('/\d\d\d\d\d\d\d\d\d\d+')
item_id =  str(p.findall(url)[0])[1:]
#print item_id
url = 'http://open.api.ebay.com/shopping?callname=GetSingleItem&itemId='
url +=  item_id
url += '&responseencoding=JSON'
url += '&appid=' + app_id
url += '&version=515'
a =json.loads(urllib2.urlopen(url).read())
print urllib2.urlopen(url).read()
print a["Item"]["ConvertedCurrentPrice"]["Value"]
