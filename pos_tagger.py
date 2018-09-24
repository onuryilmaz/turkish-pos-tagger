# -*- coding: cp1254 -*-

# Onur Yilmaz

# Imports
from .Tagger import Tagger

# Open the file where tagger is saved
taggerFileName = 'my_tagger.yaml'
myTagger = Tagger.load(taggerFileName)

# Keep the original functionality intact
def tag(sentence):
    return myTagger.tag(sentence)

# End of code
