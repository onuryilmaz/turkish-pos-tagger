# -*- coding: cp1254 -*-

# Onur Yilmaz

# Imports
import random

import yaml
from nltk.corpus.reader import TaggedCorpusReader
from nltk.tokenize import BlanklineTokenizer

# Brill tagger parameters
max_rules = 500
min_score = 5

# Training parameters
development_size = 5110
train = .50

# Import tagger
f = open('my_tagger.yaml')
myTagger = yaml.load(f)

# Read data from development.sdx
data = TaggedCorpusReader('.', r'.*\.sdx', sep='|', sent_tokenizer=BlanklineTokenizer(), encoding='ISO-8859-9')

# Get the list of tagged sentences
tagged_data = data.tagged_sents()

# Lower words and return as a list
tagged_data_list = [[t for t in sent] for sent in tagged_data]
tagged_data_list = [[(w.lower(), t) for (w, t) in s] for s in tagged_data_list]

# print "Data is read! "

# 10 steps
for i in range(1, 50):
    # Random splitting
    random.seed(len(tagged_data_list))
    random.shuffle(tagged_data_list, random.random)
    cutoff = int(development_size * train)
    training_data = tagged_data_list[:cutoff]
    evaulation_data = tagged_data_list[cutoff:development_size]

    # Evaluation 
    print "Accuracy: "
    print myTagger.evaluate(evaulation_data)

    i = i + 1

# End of code
