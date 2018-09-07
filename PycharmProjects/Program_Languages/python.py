import urllib.request
from bs4 import BeautifulSoup
import mysql.connector


quote_page = 'https://en.wikipedia.org/wiki/List_of_programming_languages'

page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')

db = mysql.connector.connect(host="localhost",     # your host, usually localhost
                     user="root",                  # your username
                     passwd="root",                # your password
                     db="languages",
                    )

cur = db.cursor()

cur.execute("delete from programs")
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
                        List = List.encode('utf-8') if isinstance(List,bytes)  else List
                        print(List)
                        insertstmt = ("insert into programs (name) VALUES ('%s')" %(List))

                cur.execute(insertstmt)
        next_div = List1.find_next('div', attrs={'class': 'div-col columns column-width'})
        List1 = next_div


        db.commit()
        goto(1)
db.close()

