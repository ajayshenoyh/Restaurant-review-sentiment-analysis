#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import re
import urllib2
from bs4 import BeautifulSoup
import os
