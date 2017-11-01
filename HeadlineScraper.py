import requests as req
from requests.packages.urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError as ce
import os
from bs4 import BeautifulSoup
from sqlite3 import Error
import sqlite3 as sql
sec=['sci-tech/','sport/','news/','opinion/','entertainment/','business/','life-and-style/','society/']
cwd = os.getcwd()
mypath = os.path.join(os.getcwd(),'Headlines')
class Headlines():
	"""Initializes a Headline Fetcher"""
	def __init__(self):
		if not os.path.exists(mypath):
			os.makedirs(mypath)
	"""
	Generic Scraper Method for the Hindu Newspaper  
	@params  arg1 The name of the class
	@params secno Section number from section array above
	@params sub1 Subsection 1 containing URL endpoint
 	@params sub2 Subsection 2 containing URL endpoint
	"""
	def runscraper(self,arg1,secno,sub1=None,sub2=None):
		arg1 = arg1[0]
		sect = sec[secno]
		for j in range(len(sub1)):
			if sub2:
				for k in range(len(sub2)):
					try:
						r = req.get('http://www.thehindu.com/'+sect+sub1[j]+sub2[k])
						if r is not None:
							self.soup = BeautifulSoup(r.content,'html.parser')
							if self.soup is not None:
								self.headline = self.soup.find('a',class_=arg1)
								if self.headline is not None:
									try:
										self.headline = self.headline.get_text().strip('\n')
										print(self.headline)
									except:
										pass	
					except (ConnectionError,ce,NewConnectionError) as e:
						print('Connection failed.')
			else:
				try:
					r = req.get('http://www.thehindu.com/'+sect+sub1[j])
					if r is not None:
							self.soup = BeautifulSoup(r.content,'html.parser')
							if self.soup is not None:
								self.headline = self.soup.find('a',class_=arg1)
								if self.headline is not None:
									self.headline = self.headline.get_text().strip('\n')
									print(self.headline)
				except (ConnectionError,ce,NewConnectionError) as e:
					print('Connection failed.')
print('----------------------------SCIENCE SECTION----------------------------')
sec1 = ['/','science/','technology/','health/','agriculture/','energy-and-environment/']
sec2 = ['gadgets/','internet/']
sciobj = Headlines()
s = ['story1-3x100-heading']
sciobj.runscraper(s,0,sub1=sec1,sub2=sec2)
# # Scrapes headlines from the Sports Section of The Hindu
print('----------------------------SPORTS SECTION----------------------------')
sec3 = ['/','cricket/','football/','hockey/','tennis/','athletics/','motorsport/']
s = ['s4x-100-ls-heading']
sportobj = Headlines()
sportobj.runscraper(s,1,sub1=sec3)
# Scrapes headlines from the News Section of The Hindu
print('----------------------------NEWS SECTION----------------------------')
sec4 = ['/','national/','international/','states/','cities/']
s = ['s4x-100-ls-heading']
newsobj = Headlines()
newsobj.runscraper(s,2,sub1=sec4)
# Scrapes headlines from the Opinion Section of The Hindu
print('----------------------------OPINION SECTION----------------------------')
sec1 = ['/','editorial/']
sec2 = ['columns/']
sec3 = ['interview/','lead/']
s = ['ES2-100x4-text1-heading']
s1 = ['column-33x3-heading left']
s2 = ['story1-3x100-heading']
opinionobj = Headlines()
opinionobj.runscraper(s,3,sub1=sec1)
opinionobj.runscraper(s1,3,sub1=sec2)
opinionobj.runscraper(s2,3,sub1=sec3)
# Scrapes headlines from the Entertainment Section of The Hindu
print('----------------------------ENTERTAINMENT SECTION----------------------------')
sec1 = ['/','music/','movies/','reviews/']
sec2 = ['theatre/','art/','dance/']
s = ['sc6-story-heading']
s1 = ['story1-3x100-heading']
entobj = Headlines()
entobj.runscraper(s,4,sub1=sec1)
# Scrapes headlines from the Business Section of The Hindu
print('----------------------------BUSINESS SECTION----------------------------')
sec1 = ['/']
sec2 = ['agri-business/','industry/','economy/','markets/','budget/']
s = ['sc6-story-heading']
s1 = ['story1-3x100-heading s1-3x100BlueBg-heading']
businessobj = Headlines()
businessobj.runscraper(s,5,sub1=sec1)
businessobj.runscraper(s1,5,sub1=sec2)
print('----------------------------LIFESTYLE SECTION----------------------------')
sec1 = ['/','fashion/','fitness/','food/','motoring/','travel/','homes-and-gardens/']
s = ['sc6-story-heading']
lifeobj = Headlines()
lifeobj.runscraper(s,6,sub1=sec1)
print('----------------------------SOCIETY SECTION----------------------------')
sec1 = ['/','faith/','history-and-culture/']
s = ['story1-3x100-heading']
socobj = Headlines()
socobj.runscraper(s,7,sub1=sec1)
print('-----------------------------------END------------------------------------')