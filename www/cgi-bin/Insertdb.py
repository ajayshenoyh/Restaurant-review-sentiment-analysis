#!C:/Python27/python
print "Content-type:text/html\r\n\r\n"
# -*- coding: utf-8 -*-
"""
basic_sentiment_analysis
~~~~~~~~~~~~~~~~~~~~~~~~
This module contains the code and examples described in 
http://fjavieralba.com/basic-sentiment-analysis-with-python.html
"""

from pprint import pprint
import nltk
import yaml
import sys
import os
import re
import MySQLdb
# Open database connection
db = MySQLdb.connect("127.0.0.1","root","","hotel" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = """CREATE TABLE HTEL (
         HTL_NAME  CHAR(100) NOT NULL,
         SCR INT )"""
sql1 = """CREATE TABLE FOODLIST (
         HTL_NAME  CHAR(100) NOT NULL,
         SCR INT )"""
sql2 = """CREATE TABLE SERVICELIST (
         HTL_NAME  CHAR(100) NOT NULL,
         SCR INT )"""
sql3 = """CREATE TABLE ENVIRONLIST (
         HTL_NAME  CHAR(100) NOT NULL,
         SCR INT )"""
sql4 = """CREATE TABLE PRICELIST (
         HTL_NAME  CHAR(100) NOT NULL,
         SCR INT )"""

#cursor.execute(sql)
#cursor.execute(sql1)
#cursor.execute(sql2)
#cursor.execute(sql3)
#cursor.execute(sql4)


class Splitter(object):

    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):

    def __init__(self):
        pass
        
    def pos_tag(self, sentences):

        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        #adapt format
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos

class DictionaryTagger(object):

    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 0
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]
                    self.max_key_size = max(self.max_key_size, len(key))

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]

    def tag_sentence(self, sentence, tag_with_lemmas=False):
        tag_sentence = []
        N = len(sentence)
        if self.max_key_size == 0:
            self.max_key_size = N
        i = 0
        while (i < N):
            j = min(i + self.max_key_size, N) #avoid overflow
            tagged = False
            while (j > i):
                expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
                expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
                if tag_with_lemmas:
                    literal = expression_lemma
                else:
                    literal = expression_form
                if literal in self.dictionary:
                    #self.logger.debug("found: %s" % literal)
                    is_single_token = j - i == 1
                    original_position = i
                    i = j
                    taggings = [tag for tag in self.dictionary[literal]]
                    tagged_expression = (expression_form, expression_lemma, taggings)
                    if is_single_token: #if the tagged literal is a single token, conserve its previous taggings:
                        original_token_tagging = sentence[original_position][2]
                        tagged_expression[2].extend(original_token_tagging)
                    tag_sentence.append(tagged_expression)
                    tagged = True
                else:
                    j = j - 1
            if not tagged:
                tag_sentence.append(sentence[i])
                i += 1
        return tag_sentence

def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0

def sentence_score(sentence_tokens, previous_token, acum_score):    
    if not sentence_tokens:
        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
                token_score /= 2.0
            elif 'inv' in previous_tags:
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])
if __name__ == "__main__":
    t=[]
    #******************************************************Overall*******************************************************************
    print("Overall Result")
    l=["C:\\wamp64\www\\reviews\\finalresult\\burgerresult.txt","C:\\wamp64\www\\reviews\\finalresult\\carlresult.txt","C:\\wamp64\www\\reviews\\finalresult\\chipotleresult.txt","C:\\wamp64\www\\reviews\\finalresult\\curryhutresult.txt","C:\\wamp64\www\\reviews\\finalresult\\mrbbqresult.txt","C:\\wamp64\www\\reviews\\finalresult\\oggiresult.txt","C:\\wamp64\www\\reviews\\finalresult\\pandaresult.txt","C:\\wamp64\www\\reviews\\finalresult\\paneraresult.txt","C:\\wamp64\www\\reviews\\finalresult\\phooliviaresult.txt","C:\\wamp64\www\\reviews\\finalresult\\pieologyresult.txt","C:\\wamp64\www\\reviews\\finalresult\\pizzapressresult.txt","C:\\wamp64\www\\reviews\\finalresult\\subwayresult.txt","C:\\wamp64\www\\reviews\\finalresult\\thaibasilresult.txt","C:\\wamp64\www\\reviews\\finalresult\\whatsupmenresult.txt"]
    for i in l:
        text = open(i,"r")
        score=0
        splitter = Splitter()
        postagger = POSTagger()
        os.chdir('C:\wamp64\lang\dicts')
        dicttagger = DictionaryTagger([ 'positive.yml', 'negative.yml', 'inc.yml', 'dec.yml', 'inv.yml'])
        for line in text:
            #print line
            splitted_sentences = splitter.split(line)
            pprint(splitted_sentences)
            pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
            pprint(pos_tagged_sentences)
            dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
            pprint(dict_tagged_sentences)
            print("analyzing sentiment...")
            score = score + sentiment_score(dict_tagged_sentences)
        print(score)
        t.append(score)
    text.close()
    #**********************************************************************Food****************************************************
    f=[]
    print("Food Result")
    fl=["C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudburgerresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudcarlresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudchipotleresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudcurryhutresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudmrbbqresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudoggiresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudpandaresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudpaneraresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudphooliviaresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudpieologyresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudpizzapressresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudsubwayresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudthaibasilresult.txt","C:\\wamp64\www\\reviews\\step1\\resultfood\\Fudwhatsupmenresult.txt"]
    for i in fl:
        text = open(i,"r")
        score=0
        splitter = Splitter()
        postagger = POSTagger()
        os.chdir('C:\wamp64\lang\dicts')
        dicttagger = DictionaryTagger([ 'positive.yml', 'negative.yml', 'inc.yml', 'dec.yml', 'inv.yml'])
        for line in text:
            #print line
            splitted_sentences = splitter.split(line)
            pprint(splitted_sentences)
            pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
            pprint(pos_tagged_sentences)
            dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
            pprint(dict_tagged_sentences)
            print("analyzing sentiment...")
            score = score + sentiment_score(dict_tagged_sentences)
        print(score)
        f.append(score)
    text.close()
    #*****************************************************************************Environment******************************************
    e=[]
    print("Environment Result")
    el=["C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envburgerresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envcarlresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envchipotleresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envcurryhutresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envmrbbqresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envoggiresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpandaresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpaneraresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envphooliviaresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpieologyresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envpizzapressresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envsubwayresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envthaibasilresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultenviron\\Envwhatsupmenresult.txt"]
    for i in el:
        text = open(i,"r")
        score=0
        splitter = Splitter()
        postagger = POSTagger()
        os.chdir('C:\wamp64\lang\dicts')
        dicttagger = DictionaryTagger([ 'positive.yml', 'negative.yml', 'inc.yml', 'dec.yml', 'inv.yml'])
        for line in text:
            #print line
            splitted_sentences = splitter.split(line)
            pprint(splitted_sentences)
            pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
            pprint(pos_tagged_sentences)
            dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
            pprint(dict_tagged_sentences)
            print("analyzing sentiment...")
            score = score + sentiment_score(dict_tagged_sentences)
        print(score)
        e.append(score)
    text.close()
    #***************************************************************************Service*****************************************************
    s=[]
    print("Service Result")
    sl=["C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serburgerresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sercarlresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serchipotleresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sercurryhutresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sermrbbqresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Seroggiresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpandaresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpaneraresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serphooliviaresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpieologyresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serpizzapressresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Sersubwayresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serthaibasilresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultservice\\Serwhatsupmenresult.txt"]
    for i in sl:
        text = open(i,"r")
        score=0
        splitter = Splitter()
        postagger = POSTagger()
        os.chdir('C:\wamp64\lang\dicts')
        dicttagger = DictionaryTagger([ 'positive.yml', 'negative.yml', 'inc.yml', 'dec.yml', 'inv.yml'])
        for line in text:
            #print line
            splitted_sentences = splitter.split(line)
            pprint(splitted_sentences)
            pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
            pprint(pos_tagged_sentences)
            dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
            pprint(dict_tagged_sentences)
            print("analyzing sentiment...")
            score = score + sentiment_score(dict_tagged_sentences)
        print(score)
        s.append(score)
    text.close()
    p=[]
    #***************************************************Price****************************************************
    print("Service Result")
    pl=["C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricburgerresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Priccarlresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricchipotleresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Priccurryhutresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricmrbbqresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricoggiresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpandaresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpaneraresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricphooliviaresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpieologyresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricpizzapressresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricsubwayresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricthaibasilresult.txt","C:\\wamp64\\www\\reviews\\step1\\resultprice\\Pricwhatsupmenresult.txt"]
    for i in pl:
        text = open(i,"r")
        score=0
        splitter = Splitter()
        postagger = POSTagger()
        os.chdir('C:\wamp64\lang\dicts')
        dicttagger = DictionaryTagger([ 'positive.yml', 'negative.yml', 'inc.yml', 'dec.yml', 'inv.yml'])
        for line in text:
            #print line
            splitted_sentences = splitter.split(line)
            pprint(splitted_sentences)
            pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
            pprint(pos_tagged_sentences)
            dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
            pprint(dict_tagged_sentences)
            print("analyzing sentiment...")
            score = score + sentiment_score(dict_tagged_sentences)
        print(score)
        p.append(score)
    text.close()
#print t[0]
sc1=t[0]
#print t[1]
sc2=t[1]
#print t[2]
sc3=t[2]
#print t[3]
sc4=t[3]
#print t[4]
sc5=t[4]
#print t[5]
sc6=t[5]
#print t[6]
sc7=t[6]
#print t[7]
sc8=t[7]
#print t[8]
sc9=t[8]
#print t[9]
sc10=t[9]
#print t[10]
sc11=t[10]
#print t[11]
sc12=t[11]
#print t[12]
sc13=t[12]
#print t[13]
sc14=t[13]
#print t[0]
##########################################################################Food##
psc1=p[0]
#print p1]
psc2=p[1]
#print p[2]
psc3=p[2]
#print p[3]
psc4=p[3]
#print p[4]
psc5=p[4]
#print p[5]
psc6=p[5]
#print p[6]
psc7=p[6]
#print p[7]
psc8=p[7]
#print p[8]
psc9=p[8]
#print p[9]
psc10=p[9]
#print p[10]
psc11=p[10]
#print p[11]
psc12=p[11]
#print p[12]
psc13=p[12]
#print p[13]
psc14=p[13]
#print f[0]
fsc1=f[0]
#print f[1]
fsc2=f[1]
#print f[2]
fsc3=f[2]
#print f[3]
fsc4=f[3]
#print f[4]
fsc5=f[4]
#print f[5]
fsc6=f[5]
#print f[6]
fsc7=f[6]
#print f[7]
fsc8=f[7]
#print f[8]
fsc9=f[8]
#print f[9]
fsc10=f[9]
#print f[10]
fsc11=f[10]
#print f[11]
fsc12=f[11]
#print f[12]
fsc13=f[12]
#print f[13]
fsc14=f[13]
#print e[0]
esc1=e[0]
#print e[1]
esc2=e[1]
#print e[2]
esc3=e[2]
#print e[3]
esc4=e[3]
#print e[4]
esc5=e[4]
#print e[5]
esc6=e[5]
#print e[6]
esc7=e[6]
#print e[7]
esc8=e[7]
#print e[8]
esc9=e[8]
#print e[9]
esc10=e[9]
#print e[10]
esc11=e[10]
#print e[11]
esc12=e[11]
#print e[12]
esc13=e[12]
#print e[13]
esc14=e[13]
#print s[0]
ssc1=s[0]
#print s[1]
ssc2=s[1]
#print s[2]
ssc3=s[2]
#print s[3]
ssc4=s[3]
#print s[4]
ssc5=s[4]
#print s[5]
ssc6=s[5]
#print s[6]
ssc7=s[6]
#print s[7]
ssc8=s[7]
#print s[8]
ssc9=s[8]
#print s[9]
ssc10=s[9]
#print s[10]
ssc11=s[10]
#print s[11]
ssc12=s[11]
#print s[12]
ssc13=s[12]
#print s[13]
ssc14=s[13]

#T0 read multiple data we st0re the reqd data in a list and pass it t0 query.
inf=[("Burger King",int(sc1)),("Carl's Jr.",int(sc2)),("Chipotle Mexican Grill",int(sc3)),("Curry Hut",int(sc4)),("Mr BBQ",int(sc5)),("Oggi's",int(sc6)),("Panda Express",int(sc7)),("Panera Bread",int(sc8)),("Pho Olivia",int(sc9))
     ,("Pieology Pizzeria",int(sc10)),("The Pizza Press",int(sc11)),("Subway",int(sc12)),("Thai Basil",int(sc13)),("What's up",int(sc14))]
inf1=[("Burger King",int(fsc1)),("Carl's Jr.",int(fsc2)),("Chipotle Mexican Grill",int(fsc3)),("Curry Hut",int(fsc4)),("Mr BBQ",int(fsc5)),("Oggi's",int(fsc6)),("Panda Express",int(fsc7)),("Panera Bread",int(fsc8)),("Pho Olivia",int(fsc9))
     ,("Pieology Pizzeria",int(fsc10)),("The Pizza Press",int(fsc11)),("Subway",int(fsc12)),("Thai Basil",int(fsc13)),("What's up",int(fsc14))]
inf2=[("Burger King",int(psc1)),("Carl's Jr.",int(psc2)),("Chipotle Mexican Grill",int(psc3)),("Curry Hut",int(psc4)),("Mr BBQ",int(psc5)),("Oggi's",int(psc6)),("Panda Express",int(psc7)),("Panera Bread",int(psc8)),("Pho Olivia",int(psc9))
     ,("Pieology Pizzeria",int(psc10)),("The Pizza Press",int(psc11)),("Subway",int(psc12)),("Thai Basil",int(psc13)),("What's up",int(psc14))]
inf3=[("Burger King",int(esc1)),("Carl's Jr.",int(esc2)),("Chipotle Mexican Grill",int(esc3)),("Curry Hut",int(esc4)),("Mr BBQ",int(esc5)),("Oggi's",int(esc6)),("Panda Express",int(esc7)),("Panera Bread",int(esc8)),("Pho Olivia",int(esc9))
     ,("Pieology Pizzeria",int(esc10)),("The Pizza Press",int(esc11)),("Subway",int(esc12)),("Thai Basil",int(esc13)),("What's up",int(esc14))]
inf4=[("Burger King",int(ssc1)),("Carl's Jr.",int(ssc2)),("Chipotle Mexican Grill",int(ssc3)),("Curry Hut",int(ssc4)),("Mr BBQ",int(ssc5)),("Oggi's",int(ssc6)),("Panda Express",int(ssc7)),("Panera Bread",int(ssc8)),("Pho Olivia",int(ssc9))
     ,("Pieology Pizzeria",int(ssc10)),("The Pizza Press",int(ssc11)),("Subway",int(ssc12)),("Thai Basil",int(ssc13)),("What's up",int(ssc14))]
try:
   # Execute the SQL command
   #cursor.execute(sql)
#this is the c0mmand t0 execute multiple inserti0ns   
   cursor.executemany("""INSERT into HTEL 
                  values (%s,%s)""",inf)
   cursor.executemany("""INSERT into FOODLIST 
                  values (%s,%s)""",inf1)
   cursor.executemany("""INSERT into SERVICELIST 
                  values (%s,%s)""",inf4)
   cursor.executemany("""INSERT into ENVIRONLIST 
                  values (%s,%s)""",inf3)
   cursor.executemany("""INSERT into PRICELIST 
                  values (%s,%s)""",inf2)
				  

   results=cursor.fetchall()
   print "Done"
   print results
   #Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
