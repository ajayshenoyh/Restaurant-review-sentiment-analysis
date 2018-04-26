#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import re
import urllib2
from bs4 import BeautifulSoup
import os
import glob

#*********************************************************************Food********************************************************
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)",re.I)  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudburgerY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)",re.I)  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')
n2=open("FudburgerT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)",re.I)  #regular exp
f2=open("bugerking.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')
n2=open("FudburgerG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("carltrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudcarlY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("carltrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudcarlT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("carls.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudcarlsG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("chipotletrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudchipotleY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("chipotletrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudchipotleT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("chipotle.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudchipotleG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("curryhuttrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudcurryhutY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("curryhuttrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudcurryhutT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("curryhut.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudcurryhutG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("mrbbqtrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudmrbbqY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("mrbbqtrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudmrbbqT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("mrbbq.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudmrbbqG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("oggitrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudoggiY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("oggitrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudoggiT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("oggis.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudoggiG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pandatrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudpandaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pandatrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudpandaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("panda.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudpandaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("paneratrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudpaneraY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("paneratrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudpaneraT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("panera.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudpaneraG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("phooliviatrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudphooliviaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("phooliviatrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudphooliviaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("phoolivia.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudphooliviaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pieologytrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudpieologyY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pieologytrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudpieologyT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pielogy.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudpieologyG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pizzapresstrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudpizzapressY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pizzapresstrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudpizzapressT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("pizzapress.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')
n2=open("FudpizzapressG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("subwaytrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudsubwayY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("subwaytrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudsubwayT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("subway.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')

n2=open("FudsubwayG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("thaibasiltrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudthaibasilY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("thaibasiltrip.txt","r")

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')

n2=open("FudthaibasilT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("thaibasil.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')
n2=open("FudthaibasilG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("whatsupmentrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
n2=open("FudwhatsupmenY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("whatsuptrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')
n2=open("FudwhatsupmenT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(food.*)|(taste.*)|(fish)|(.*drink.*)|(lunch.*)|(breakf.*)|(dinner.*)",re.I)  #regular exp
f2=open("whatsupmen.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')
n2=open("FudwhatsupmenG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

#**********************************SERVICE***********************************
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("subwaytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SersubwayY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("subwaytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SersubwayT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("subway.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SersubwayG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerburgerY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerburgerT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("bugerking.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerburgerG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("carltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SercarlY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("carltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SercarlT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("carls.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SercarlG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("chipotletrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerchipotleY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("chipotletrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerchipotleT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("chipotle.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerchipotleG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("curryhuttrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SercurryhutY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("curryhuttrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SercurryhutT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("curryhut.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SercurryhutG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("mrbbqtrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SermrbbqY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("mrbbqtrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SermrbbqT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("mrbbq.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SermrbbqG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("oggitrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SeroggiY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("oggitrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SeroggiT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("oggis.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SeroggiG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pandatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerpandaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pandatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerpandaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("panda.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerpandaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("paneratrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerpaneraY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("paneratrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerpaneraT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("panera.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerpaneraG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("phooliviatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerphooliviaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("phooliviatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerphooliviaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("phoolivia.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerphooliviaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pieologytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerpieologyY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pieologytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerpieologyT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pielogy.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerpieologyG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pizzapresstrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerpizzapressY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pizzapresstrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerpizzapressT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("pizzapress.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerpizzapressG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("thaibasiltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerthaibasilY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("thaibasiltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerthaibasilT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("thaibasil.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerthaibasilG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("whatsupmentrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
n2=open("SerwhatsupmenY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("whatsuptrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
n2=open("SerwhatsupmenT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(staff.*)|(service.*)|(hospitality.*)|(desk.*)|(manager.*)",re.I)  #regular exp
f2=open("whatsupmen.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
n2=open("SerwhatsupmenG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

print "dne SERVICE"
#*********************************************************************Price********************************************************

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("subwaytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricsubwayY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("subwaytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricsubwayT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("subway.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricsubwayG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricburgerY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricburgerT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("bugerking.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricburgerG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("carltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PriccarlY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("carltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PriccarlT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("carls.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PriccarlG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("chipotletrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricchipotleY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("chipotletrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricchipotleT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("chipotle.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricchipotleG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("curryhuttrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PriccurryhutY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("curryhuttrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PriccurryhutT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("curryhut.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PriccurryhutG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("mrbbqtrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricmrbbqY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("mrbbqtrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricmrbbqT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("mrbbq.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricmrbbqG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("oggitrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricoggiY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("oggitrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricoggiT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("oggis.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricoggiG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pandatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricpandaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pandatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricpandaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("panda.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricpandaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("paneratrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricpaneraY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("paneratrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricpaneraT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("panera.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricpaneraG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("phooliviatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricphooliviaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("phooliviatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricphooliviaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("phoolivia.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricphooliviaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pieologytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricpieologyY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pieologytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricpieologyT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pielogy.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricpieologyG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pizzapresstrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricpizzapressY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pizzapresstrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricpizzapressT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("pizzapress.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricpizzapressG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("thaibasiltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricthaibasilY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("thaibasiltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricthaibasilT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("thaibasil.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricthaibasilG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("whatsupmentrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
n2=open("PricwhatsupmenY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("whatsuptrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
n2=open("PricwhatsupmenT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(price.*)|(cost.*)|(expens.*)",re.I)  #regular exp  #regular exp
f2=open("whatsupmen.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
n2=open("PricwhatsupmenG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
####################################################################################################
#******************************************ENvironemnt***************************************
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("subwaytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvsubwayY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("subwaytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvsubwayT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("subway.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvsubwayG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvburgerY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("burgertrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvburgerT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("bugerking.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvburgerG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("carltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvcarlY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("carltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvcarlT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("carls.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvcarlG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("chipotletrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvchipotleY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("chipotletrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvchipotleT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("chipotle.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvchipotleG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("curryhuttrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvcurryhutY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("curryhuttrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvcurryhutT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("curryhut.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvcurryhutG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("mrbbqtrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvmrbbqY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("mrbbqtrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvmrbbqT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("mrbbq.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvmrbbqG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("oggitrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvoggiY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("oggitrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvoggiT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("oggis.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvoggiG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pandatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvpandaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pandatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvpandaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("panda.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvpandaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("paneratrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvpaneraY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("paneratrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvpaneraT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("panera.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvpaneraG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("phooliviatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvphooliviaY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("phooliviatrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvphooliviaT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("phoolivia.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvphooliviaG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pieologytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvpieologyY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pieologytrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvpieologyT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pielogy.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvpieologyG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pizzapresstrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvpizzapressY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pizzapresstrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvpizzapressT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("pizzapress.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvpizzapressG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("thaibasiltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvthaibasilY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("thaibasiltrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvthaibasilT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("thaibasil.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvthaibasilG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("whatsupmentrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
n2=open("EnvwhatsupmenY.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()

os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("whatsuptrip.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
n2=open("EnvwhatsupmenT.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()
os.chdir('C:\\wamp64\www\\reviews\\googlereviews')
pattern=re.compile("(enviro.*)|(surround.*)|(place.*)|(beach.*)",re.I)  #regular exp
f2=open("whatsupmen.txt","r")
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
n2=open("EnvwhatsupmenG.txt","w+")
for line in f2:
    #print line
    #line=line.strip()
    if re.search(pattern,line):
        n2.write(line)
n2.close()
f2.close()


print "dne ENVI"

############################################################
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\food')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
			
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\environ')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\price')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
os.chdir('C:\\wamp64\www\\reviews\\googlereviews\\service')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

############################################3
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\food')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
			
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\environ')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\price')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
os.chdir('C:\\wamp64\www\\reviews\\yelp\\trimtext\\service')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
################################################3
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\food')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
			
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\environ')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\price')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
os.chdir('C:\\wamp64\www\\reviews\\trip\\trimtext\\service')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
############################################
#COmbining reviews from yelp,google,tripadvisor
os.chdir('C:\\wamp64\www\\reviews')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\result.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\result.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\result.txt' ]
with open('Evnresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\result.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\result.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\result.txt' ]
with open('Foodresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\result.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\result.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\result.txt' ]
with open('Servresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\result.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\result.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\result.txt' ]
with open('Pricresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
