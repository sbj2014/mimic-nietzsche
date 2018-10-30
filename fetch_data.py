"""
fetch_data module
28 October 2018
"""

# scrape data from website

def acquire_data(source):

	import urllib2
	from bs4 import BeautifulSoup

	req = urllib2.Request(source)
	response = urllib2.urlopen(req)

	text = response.read()

	response.close()

	text = BeautifulSoup(text, "html.parser").get_text(strip=True)
	return text
