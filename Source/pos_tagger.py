# -*- coding: cp1254 -*-

# Onur Yilmaz

# Imports
import codecs
import locale
import bisect        
import random
import sys
import yaml           
import textwrap 
from nltk.tokenize import BlanklineTokenizer
from nltk.corpus.reader import TaggedCorpusReader
from random import shuffle
from nltk.corpus import treebank 
from nltk import tag 
from nltk.tag import brill
 
# Open the file where tagger is saved
f=open('my_tagger.yaml')
myTagger=yaml.load(f)

# Tagger function
def tag(sentence):
    # Lower input
    temp = [[t.lower()] for t in sentence.split()]
    return_list = []
    # Find tags
    for token in temp:
        return_list.append(myTagger.tag(token))
    
    return_list = [t for [t] in return_list]
    # Correct tags for printing
    tag_list = [y for (x,y) in return_list]
    tag_list = [(y.lower()).title() for y in tag_list]

    # Zip input and tags
    temp_list = zip([t for t in sentence.split()], tag_list)

    return temp_list

# End of code

