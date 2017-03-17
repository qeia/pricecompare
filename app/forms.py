from django import forms

class ItemInfo(forms.Form):
	asin = forms.CharField(required=True,label="ASIN (ID) of the item")
	gamestopurl = forms.CharField(required=True,label = "Gamestop url of the item")
	walmartid = forms.CharField(required=True,label = "Walmart ID of the item")
	ebayurl = forms.CharField(required=True,label = "Enter ebay URL")
	bestbuyurl = forms.CharField(required=True,label = "Enter bestbuy URl")
	