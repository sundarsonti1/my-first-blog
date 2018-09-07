import urllib2
from bs4 import BeautifulSoup


quote_page = 'https://en.wikipedia.org/wiki/List_of_programming_languages'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')

List1 = soup.find('div',attrs = {'class':'div-col columns column-width'})
def goto(linenum):
    global line
    line = linenum
line = 1
while True:
	if List1 == None:
		break
	
	else:
		List_box = List1.find_all('li')
		for b in List_box:
			List= b.text.strip()
			List = List.encode('utf-8') if isinstance(List,unicode)  else List
			print List
		next_div = List1.find_next('div',attrs= {'class': 'div-col columns column-width'})
		List1 = next_div
	goto(1)

