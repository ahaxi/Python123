import urllib, urllib2
import re
from pythonTools import UnicodeWriter
from bs4 import BeautifulSoup

# Web scrapy to download all the company reviews

baseurl = "http://www.glassdoor.com/Reviews/somecompany"
username = 'secret'
password = 'secret'
params = urllib.urlencode(dict(username=username, password=password))

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4)'
headers = { 'User-Agent' : user_agent }

f = UnicodeWriter(open("glassdoorResult.txt", "w"), delimiter = "\t")
f.writerow(["id","page","time","review_title","rating","jobtitle", "location", "pros", "cons", "advice"])
pagenumber = # Find a pattern for the webpages you want to get, or follow some link
count = 0
for i in range(1, pagenumber):
	if i == 1:
		url = baseurl + ".htm"
	else:
		url = baseurl + "_P" + str(i) + ".htm"

	req = urllib2.Request(url, params, headers)
	response = urllib2.urlopen(req)
	webpg = response.read()
	soup = BeautifulSoup(webpg)

	res = soup.find_all('li', {'class': 'empReview padVert cf '})
	for r in res:
		count += 1
		time = r.find_all('time')[0].get_text()
		title  = r.find_all('span', {'class':'summary'})[0].get_text()
		rating = r.find_all('span', {'class':'value-title'})[0]['title']
		jobtitle = r.find_all('span', {'class':'authorJobTitle padLtSm'})[0].get_text()
		
		if r.find_all('span', {'class':'authorLocation i-loc'}):
			location = r.find_all('span', {'class':'authorLocation i-loc'})[0].get_text()
			location = re.sub(' in', '', location)
		else:
			location = ""

		if r.find_all('p', {'class':'pros noMargVert '}):
			pros = r.find_all('p', {'class':'pros noMargVert '})[0].get_text()
		else:
			pros = ""

		if r.find_all('p', {'class':'cons noMargVert '}):
			cons = r.find_all('p', {'class':'cons noMargVert '})[0].get_text()
		else:
			cons = ""
		
		try:
			if r.find_all('p', {'class':'adviceMgmt noMargVert '}):
				advice = r.find_all('p', {'class':'adviceMgmt noMargVert '})[0].get_text()
			else:
				advice = ""
		except:
			print count, i
		pageid = "g_" + str(count)
		f.writerow([pageid, str(i), time, title, rating, jobtitle, location, pros, cons, advice])

#############################################




