
url = 'http://svcs.ebay.com/services/search/FindingService/v1?'
url+='OPERATION-NAME=findItemsByProduct&'
url+='SERVICE-VERSION=1.0.0&'
url+='SECURITY-APPNAME=Benjamin-products-PRD-92466ad44-13674f29&'
url+='RESPONSE-DATA-FORMAT=XML&'
url+='REST-PAYLOAD&'
url+='paginationInput.entriesPerPage=2&'
url+='ProductId.@type=Reference&'
url+='ProductId=53039031'


print url


http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=Benjamin-products-PRD-92466ad44-13674f29&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&paginationInput.entriesPerPage=2&productId.@type=ReferenceID&productId=167317351
http://svcs.ebay.com/services/search/FindingService/v1?SECURITY-APPNAME=Benjamin-products-PRD-92466ad44-13674f29&OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&productId.@type=UPC&productId=883929106646&paginationInput.entriesPerPage=3	
http://svcs.ebay.com/services/search/FindingService/v1?SECURITY-APPNAME=Benjamin-products-PRD-92466ad44-13674f29&OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&productId.@type=UPC&productId=167317351&paginationInput.entriesPerPage=3	

4549576006192
http://open.api.ebay.com/shopping?callname=FindProducts&responseencoding=XML&appid=Benjamin-products-PRD-92466ad44-13674f29&siteid=0&version=967&QueryKeywords=playstation&AvailableItemsOnly=true&MaxEntries=2
http://svcs.ebay.com/services/search/FindingService/v1?SECURITY-APPNAME=Benjamin-products-PRD-92466ad44-13674f29&OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&productId.@type=UPC&ReferenceID=230282797&paginationInput.entriesPerPage=3
http://open.api.ebay.com/shopping?callname=GetSingleItem&itemId=231525785891&appid=Benjamin-products-PRD-92466ad44-13674f29&version=515
url = 'http://open.api.ebay.com/shopping?callname=GetSingleItem&itemId='
url +=  item_id
url += '&appid' + app_id
url += '&version=515'


