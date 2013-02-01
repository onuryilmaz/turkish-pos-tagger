# -*- coding: cp1254 -*-

# Onur Yilmaz
# 1627868
# CENG 463 - HW 2

# Imports
import locale
import bisect        
import random        
import yaml           
import textwrap 
from nltk.tokenize import BlanklineTokenizer
from nltk.corpus.reader import TaggedCorpusReader
from random import shuffle
from nltk.corpus import treebank 
from nltk import tag 
from nltk.tag import brill
from pos_tagger import tag

# Brill tagger parameters
max_rules=500
min_score=5

# Training parameters
development_size=5110
train=.50

# Import tagger
f=open('my_tagger.yaml')
myTagger=yaml.load(f)


# Read data from development.sdx
data = TaggedCorpusReader('.', r'.*\.sdx',  sep='|', sent_tokenizer=BlanklineTokenizer(),tag_mapping_function=None)

# Get the list of tagged sentences
tagged_data = data.tagged_sents()


# Lower words and return as a list
tagged_data_list  = [[t for t in sent] for sent in tagged_data] 
tagged_data_list = [[(w.lower(),t) for (w,t) in s] for s in tagged_data_list]

## print "Data is read! " 

# 10 steps
for i in range(1,50):

    # Random splitting
    random.seed(len(tagged_data_list)) 
    random.shuffle(tagged_data_list,random.random) 
    cutoff = int(development_size*train) 
    training_data = tagged_data_list[:cutoff] 
    evaulation_data = tagged_data_list[cutoff:development_size] 

    # Evaluation 
    print "Accuracy: "
    print myTagger.evaluate(evaulation_data)

    i = i+1

# End of code
