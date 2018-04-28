import json
import re
import requests
from bs4 import BeautifulSoup

r= requests.get("https://stockx.com/adidas-ultra-boost-4-undftd-white")
soup=BeautifulSoup(r.content,"html.parser")

pattern=re.compile("lowPrice")

#print soup.findAll("script", type="application/ld+json")
for data in soup.find_all("script"):
	match=pattern.search(data.text)
	if match:
		offer=json.loads(data.text)
		print offer['offers']['offers'][8]['price']
		#print offer['offers']['offers'][0]['price']
		#j=json.loads(data.text)
		#print offer['offers'][0]

#for key, value in offer.items():
#	print (key,value)
#print offer.keys()
