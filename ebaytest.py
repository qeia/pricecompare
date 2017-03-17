from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

api = Finding(appid="Benjamin-products-PRD-92466ad44-13674f29", config_file=None)
response = api.execute('FindProducts', {'ProductId': {'#attr:':{'type':'USBN'}, '#text': '0596154488'}})
print response.dict()

