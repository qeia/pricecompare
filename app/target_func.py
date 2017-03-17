def target(self,url):
		browser = webdriver.PhantomJS()
		browser.get(url)
		src = browser.page_source
		soup = BeautifulSoup(src,"lxml")
		a = soup.find_all('div',class_='price')[0]
		b=str(a)
		p = re.compile('\$[\d.,]+')
		price = p.findall(b)
		price = price[0]
		available=False
		c=soup.find_all('button',class_='sbc-add-to-cart btn btn-primary btn-lg btn-block sbc-selected')
		if len(c)>0 and "add to cart" in str(c[0]):
			available = True
		c=soup.find_all('button',class_='btn btn-default btn-lg btn-block btn-disabled is-disabled')
		if len(c)>0 and "only in stores" in str(c[0]):
			available=False
		if len(price)>1:
			"found price"
		return float(price[1:]),available