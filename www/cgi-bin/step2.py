#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import re
import urllib2
from bs4 import BeautifulSoup
import os
#**********************Total restaurant************************
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envburgerresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudburgerresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serburgerresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricburgerresult.txt' ]
with open('burgerresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envcarlresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudcarlresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sercarlresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Priccarlresult.txt' ]
with open('carlresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envchipotleresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudchipotleresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serchipotleresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricchipotleresult.txt' ]
with open('chipotleresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envcurryhutresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudcurryhutresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sercurryhutresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Priccurryhutresult.txt' ]
with open('curryhutresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envmrbbqresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudmrbbqresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sermrbbqresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricmrbbqresult.txt' ]
with open('mrbbqresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envoggiresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudoggiresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Seroggiresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricoggiresult.txt' ]
with open('oggiresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpandaresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudpandaresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpandaresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpandaresult.txt' ]
with open('pandaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpaneraresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudpaneraresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpaneraresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpaneraresult.txt' ]
with open('paneraresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envphooliviaresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudphooliviaresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serphooliviaresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricphooliviaresult.txt' ]
with open('phooliviaresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpieologyresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudpieologyresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpieologyresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpieologyresult.txt' ]
with open('pieologyresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpizzapressresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudpizzapressresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpizzapressresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpizzapressresult.txt' ]
with open('pizzapressresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envsubwayresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudsubwayresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sersubwayresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricsubwayresult.txt' ]
with open('subwayresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envthaibasilresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudthaibasilresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serthaibasilresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricthaibasilresult.txt' ]
with open('thaibasilresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
os.chdir('C:\\wamp64\www\\reviews\\finalresult')
filenames = ['C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envwhatsupmenresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultfood\\Fudwhatsupmenresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serwhatsupmenresult.txt', 'C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricwhatsupmenresult.txt' ]
with open('whatsupmenresult.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)				