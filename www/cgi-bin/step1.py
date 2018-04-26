#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import re
import urllib2
from bs4 import BeautifulSoup
import os
#****************************************FOOD COMBINATION**************************************************
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultfood')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudburgerT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudburgerG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudburgerY.txt' ]
with open('Fudburgerresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudcarlT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudcarlG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudcarlY.txt' ]
with open('Fudcarlresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudchipotleT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudchipotleG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudchipotleY.txt' ]
with open('Fudchipotleresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudcurryhutT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudcurryhutG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudcurryhutY.txt' ]
with open('Fudcurryhutresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudmrbbqT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudmrbbqG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudmrbbqY.txt' ]
with open('Fudmrbbqresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudoggiT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudoggiG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudoggiY.txt' ]
with open('Fudoggiresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudpandaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudpandaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudpandaY.txt' ]
with open('Fudpandaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudpaneraT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudpaneraG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudpaneraY.txt' ]
with open('Fudpaneraresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudphooliviaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudphooliviaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudphooliviaY.txt' ]
with open('Fudphooliviaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudpieologyT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudpieologyG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudpieologyY.txt' ]
with open('Fudpieologyresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudpizzapressT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudpizzapressG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudpizzapressY.txt' ]
with open('Fudpizzapressresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudsubwayT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudsubwayG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudsubwayY.txt' ]
with open('Fudsubwayresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudthaibasilT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudthaibasilG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudthaibasilY.txt' ]
with open('Fudthaibasilresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\food\\FudwhatsupmenT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\food\\FudwhatsupmenG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\food\\FudwhatsupmenY.txt' ]
with open('Fudwhatsupmenresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
#***********************************************************Service COMBINATION**************************************************
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerburgerT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerburgerG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerburgerY.txt' ]
with open('Serburgerresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SercarlT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SercarlG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SercarlY.txt' ]
with open('Sercarlresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerchipotleT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerchipotleG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerchipotleY.txt' ]
with open('Serchipotleresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SercurryhutT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SercurryhutG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SercurryhutY.txt' ]
with open('Sercurryhutresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SermrbbqT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SermrbbqG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SermrbbqY.txt' ]
with open('Sermrbbqresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SeroggiT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SeroggiG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SeroggiY.txt' ]
with open('Seroggiresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerpandaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerpandaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerpandaY.txt' ]
with open('Serpandaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerpaneraT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerpaneraG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerpaneraY.txt' ]
with open('Serpaneraresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerphooliviaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerphooliviaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerphooliviaY.txt' ]
with open('Serphooliviaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerpieologyT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerpieologyG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerpieologyY.txt' ]
with open('Serpieologyresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerpizzapressT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerpizzapressG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerpizzapressY.txt' ]
with open('Serpizzapressresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SersubwayT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SersubwayG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SersubwayY.txt' ]
with open('Sersubwayresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerthaibasilT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerthaibasilG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerthaibasilY.txt' ]
with open('Serthaibasilresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultservice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\service\\SerwhatsupmenT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\service\\SerwhatsupmenG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\service\\SerwhatsupmenY.txt' ]
with open('Serwhatsupmenresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
#*******************************************************************PRICE COMBINATION**************************************************
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricburgerT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricburgerG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricburgerY.txt' ]
with open('Pricburgerresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PriccarlT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PriccarlG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PriccarlY.txt' ]
with open('Priccarlresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricchipotleT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricchipotleG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricchipotleY.txt' ]
with open('Pricchipotleresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PriccurryhutT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PriccurryhutG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PriccurryhutY.txt' ]
with open('Priccurryhutresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricmrbbqT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricmrbbqG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricmrbbqY.txt' ]
with open('Pricmrbbqresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricoggiT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricoggiG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricoggiY.txt' ]
with open('Pricoggiresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricpandaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricpandaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricpandaY.txt' ]
with open('Pricpandaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricpaneraT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricpaneraG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricpaneraY.txt' ]
with open('Pricpaneraresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricphooliviaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricphooliviaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricphooliviaY.txt' ]
with open('Pricphooliviaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricpieologyT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricpieologyG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricpieologyY.txt' ]
with open('Pricpieologyresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricpizzapressT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricpizzapressG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricpizzapressY.txt' ]
with open('Pricpizzapressresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricsubwayT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricsubwayG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricsubwayY.txt' ]
with open('Pricsubwayresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricthaibasilT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricthaibasilG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricthaibasilY.txt' ]
with open('Pricthaibasilresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultprice')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\price\\PricwhatsupmenT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\price\\PricwhatsupmenG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\price\\PricwhatsupmenY.txt' ]
with open('Pricwhatsupmenresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
#**********************************************************Environment COMBINATION**************************************************
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvburgerT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvburgerG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvburgerY.txt' ]
with open('Envburgerresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvcarlT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvcarlG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvcarlY.txt' ]
with open('Envcarlresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvchipotleT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvchipotleG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvchipotleY.txt' ]
with open('Envchipotleresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvcurryhutT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvcurryhutG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvcurryhutY.txt' ]
with open('Envcurryhutresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvmrbbqT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvmrbbqG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvmrbbqY.txt' ]
with open('Envmrbbqresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvoggiT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvoggiG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvoggiY.txt' ]
with open('Envoggiresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvpandaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvpandaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvpandaY.txt' ]
with open('Envpandaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvpaneraT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvpaneraG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvpaneraY.txt' ]
with open('Envpaneraresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvphooliviaT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvphooliviaG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvphooliviaY.txt' ]
with open('Envphooliviaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvpieologyT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvpieologyG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvpieologyY.txt' ]
with open('Envpieologyresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvpizzapressT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvpizzapressG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvpizzapressY.txt' ]
with open('Envpizzapressresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvsubwayT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvsubwayG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvsubwayY.txt' ]
with open('Envsubwayresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvthaibasilT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvthaibasilG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvthaibasilY.txt' ]
with open('Envthaibasilresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\step1\\resultenviron')
filenames = ['C:\wamp64\\www\\reviews\\trip\\trimtext\\environ\\EnvwhatsupmenT.txt', 'C:\\wamp64\\www\\reviews\\googlereviews\\environ\\EnvwhatsupmenG.txt', 'C:\\wamp64\\www\\reviews\\yelp\\trimtext\\environ\\EnvwhatsupmenY.txt' ]
with open('Envwhatsupmenresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
			