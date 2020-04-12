import requests 
from bs4 import BeautifulSoup
import html5lib

term= input("Type to search: ")
url= "https://en.wikipedia.org/wiki/"+term
r= requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
p =soup.findAll("p")
print(p[1].text)
#print(soup.prettify())