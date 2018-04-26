#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import re
import urllib2
from bs4 import BeautifulSoup
import os
#**************************Web scrapping*******************************
os.chdir('C:\\wamp64\www\\reviews\\trip')
f1=open("thai_url.txt","r") #TRIP ADVISOR
f2=open("thai.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("burgerking_url.txt","r") #TRIP ADVISOR
f2=open("burger.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("carl_url.txt","r") #TRIP ADVISOR
f2=open("carl.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("chipotle_url.txt","r") #TRIP ADVISOR
f2=open("chipotle.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("curryhut_url.txt","r") #TRIP ADVISOR
f2=open("curryhut.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("mrbbq_url.txt","r") #TRIP ADVISOR
f2=open("mrbbq.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("oggi_url.txt","r") #TRIP ADVISOR
f2=open("oggi.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("panda_url.txt","r") #TRIP ADVISOR
f2=open("panda.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("panera_url.txt","r") #TRIP ADVISOR
f2=open("panera.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("phoolivia_url.txt","r") #TRIP ADVISOR
f2=open("phoolivia.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("pieology_url.txt","r") #TRIP ADVISOR
f2=open("pieology.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("pizzapress_url.txt","r") #TRIP ADVISOR
f2=open("pizzapress.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("subway_url.txt","r") #TRIP ADVISOR
f2=open("subway.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("whatsup_url.txt","r") #TRIP ADVISOR
f2=open("whatsup.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'class': 'partial_entry'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

#*****************************YELP Scraping************************
os.chdir('C:\\wamp64\www\\reviews\\yelp')
f1=open("thaibasil_url.txt","r") #Yelp
f2=open("thai.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("bugerking_url.txt","r") #Yelp
f2=open("burger.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("carl_url.txt","r") #Yelp
f2=open("carl.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("chipotle_url.txt","r") #Yelp
f2=open("chipotle.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("curryhut_url.txt","r") #Yelp
f2=open("curryhut.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("jersey_url.txt","r") #Yelp
f2=open("jersey.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("mrbbq_url.txt","r") #Yelp
f2=open("mrbbq.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("oggi_url.txt","r") #Yelp
f2=open("oggi.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("panda_url.txt","r") #Yelp
f2=open("panda.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("panera_url.txt","r") #Yelp
f2=open("panera.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("phoolivia_url.txt","r") #Yelp
f2=open("phoolivia.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("pieology_url.txt","r") #Yelp
f2=open("pieology.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("pizzapress_url.txt","r") #Yelp
f2=open("pizzapress.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("quickly_url.txt","r") #Yelp
f2=open("quickly.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("subway_url.txt","r") #Yelp
f2=open("subway.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("thailandia_url.txt","r") #Yelp
f2=open("thailandia.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()

f1=open("whatsupmen_url.txt","r") #Yelp
f2=open("whatsupmen.txt","r+")
for url in f1:
    soup=BeautifulSoup(urllib2.urlopen(url))
    soup.prettify()
    for each_div in soup.findAll('p', {'itemprop': 'description'}):
         f2.write(str(each_div));
    #let = soup.find_all("p", class_="partial_entry")
    #print let
    
f2.close()
f1.close()
