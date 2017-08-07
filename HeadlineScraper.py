import requests as req
from bs4 import BeautifulSoup
# Scrapes headlines from the Science Section of The Hindu
print('----------------------------SCIENCE SECTION----------------------------')
sec = ['','science','technology','health','agriculture','energy-and-environment']
sec2 = ['','gadgets','internet']
for item in range(len(sec)):
	try:
	    r = req.get('http://www.thehindu.com/sci-tech/'+sec[item]+'/')
	    if item == 'technology':
	    	r = req.get('http://www.thehindu.com/sci-tech/technology/')
	    	for spl in range(len(sec2)):
	    		r = req.get('http://www.thehindu.com/sci-tech/technology/'+sec2[spl]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main1 = soup.find("a",class_="story1-3x100-heading").get_text().strip('\n')
	    print(main1)    
	except ConnectionError:
		print('Connection Failed.') 
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')	

# Scrapes headlines from the Sports Section of The Hindu
print('----------------------------SPORTS SECTION----------------------------')
sec = ['','cricket','football','hockey','tennis','athletics']
for item in range(len(sec)):
	try:
	    r = req.get('http://www.thehindu.com/sport/'+sec[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main2 = soup.find("a",class_="s4x-100-ls-heading").get_text().strip('\n')
	    print(main2)    
	except ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')
# Scrapes headlines from the News Section of The Hindu
print('----------------------------NEWS SECTION----------------------------')
sec = ['','national','international','states','cities']
for item in range(len(sec)):
	try:
	    r = req.get('http://www.thehindu.com/news/'+sec[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main3 = soup.find("a",class_="s4x-100-ls-heading").get_text().strip('\n')
	    print(main3)    
	except requests.exceptions.ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')
# Scrapes headlines from the Opinion Section of The Hindu
print('----------------------------OPINION SECTION----------------------------')
sec1 = ['','editorial']
sec2 = ['interview','lead']
for item in range(len(sec1)):
	try:
	    r = req.get('http://www.thehindu.com/opinion/'+sec1[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main4 = soup.find("a",class_="ES2-100x4-text1-heading").get_text().strip('\n')
	    print(main4)
	    r = req.get('http://www.thehindu.com/opinion/columns/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main5 = soup.find("a",class_="column-33x3-heading left").get_text().strip('\n')
	    print(main5)
	    r = req.get('http://www.thehindu.com/opinion/'+sec2[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main6 = soup.find("a",class_="story1-3x100-heading").get_text().strip('\n')
	    print(main6)    
	except requests.exceptions.ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')
# Scrapes headlines from the Entertainment Section of The Hindu
print('----------------------------ENTERTAINMENT SECTION----------------------------')
sec1 = ['','music','movies','reviews']
sec2 = ['art','dance']
for item in range(len(sec1)):
	try:
	    r = req.get('http://www.thehindu.com/entertainment/'+sec1[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main7 = soup.find("a",class_="sc6-story-heading").get_text().strip('\n')
	    print(main7)
	except requests.exceptions.ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')		       
for item in range(len(sec2)):
	try:
	    r = req.get('http://www.thehindu.com/entertainment/'+sec2[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main8 = soup.find("a",class_="story1-3x100-heading").get_text().strip('\n')
	    print(main8)  	     
	except requests.exceptions.ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')
# Scrapes headlines from the Business Section of The Hindu
print('----------------------------BUSINESS SECTION----------------------------')
sec1 = ['']
sec2 = ['agri-business','industry','economy','markets']
for item in range(len(sec1)):
	try:
	    r = req.get('http://www.thehindu.com/business/'+sec1[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main7 = soup.find("a",class_="sc6-story-heading").get_text().strip('\n')
	    print(main7)
	except requests.exceptions.ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')		       
for item in range(len(sec2)):
	try:
	    r = req.get('http://www.thehindu.com/business/'+sec2[item]+'/')    		
	    soup = BeautifulSoup(r.content,'html.parser')
	    main9 = soup.find("a",class_="story1-3x100-heading s1-3x100BlueBg-heading").get_text().strip('\n')
	    print(main9)  	     
	except requests.exceptions.ConnectionError:
		print('Connection Failed.')
	except requests.packages.urllib3.exceptions.NewConnectionError:
		print('Connection Failed.')
print('-----------------------------------END------------------------------------')