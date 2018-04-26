#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import re
import urllib2
from bs4 import BeautifulSoup
import os

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("burger.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("burgertrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("burger.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("burgertrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("carl.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("carltrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("carl.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("carltrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("chipotle.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("chipotletrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("chipotle.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("chipotletrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("curryhut.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("curryhuttrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("curryhut.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("curryhuttrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("mrbbq.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("mrbbqtrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("mrbbq.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("mrbbqtrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("oggi.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("oggitrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("oggi.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("oggitrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("panda.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("pandatrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("panda.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("pandatrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("panera.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("paneratrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("panera.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("paneratrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("phoolivia.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("phooliviatrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("phoolivia.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("phooliviatrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("pieology.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("pieologytrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("pieology.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("pieologytrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("pizzapress.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("pizzapresstrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("pizzapress.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("pizzapresstrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("subway.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("subwaytrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("subway.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("subwaytrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("thai.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("thaibasiltrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("thai.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("thaibasiltrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\trip')
f1=open("whatsup.txt","r")  #removing extras of trip
os.chdir('C:\\wamp64\\www\\reviews\\trip\\trimtext')
n1=open("whatsuptrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()

os.chdir('C:\\wamp64\\www\\reviews\\yelp')
f1=open("whatsupmen.txt","r")  #removing extras of yelp
os.chdir('C:\\wamp64\\www\\reviews\\yelp\\trimtext')
n1=open("whatsupmentrip.txt","w+")
for line in f1:
    rep=re.sub("<.*","",line)
    match=re.sub("[.,/<;!]|(but)",". \n",rep)
    n1.write(match)
f1.close()
n1.close()