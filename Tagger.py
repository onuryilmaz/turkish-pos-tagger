# -*- coding: cp1254 -*-

# Onur Yilmaz

# Imports
import yaml
import os
from nltk.tag.brill import BrillTagger

from yaml.parser import ParserError

class Tagger:
    def __init__(self, tagger):
        self.myTagger = tagger

    @classmethod
    def load(cls, modelFile):
        if not os.path.exists(modelFile):
            raise FileNotFoundError("The model file: {} not found.".format(modelFile))
        try:
            with open(modelFile) as file:
                myTagger = yaml.load(file)
            if not isinstance(myTagger, BrillTagger):
                raise TypeError("The model file: {} could not be loaded as a nltk.tag.brill.BrillTagger object".format(
                    modelFile
                ))
            return cls(myTagger)
        except ParserError as error:
            print(error)
            raise TypeError("Could not load file {} as yaml file.".format(modelFile))

    # Tagger function
    def tag(self, sentence):
        if not isinstance(sentence, str):
            raise TypeError("Input sentence has to be of type str. Is of type {}".format(type(sentence)))
        # Lower input
        temp = [[t.lower()] for t in sentence.split()]
        return_list = []
        # Find tags
        for token in temp:
            return_list.append(self.myTagger.tag(token))

        return_list = [t for [t] in return_list]
        # Correct tags for printing
        tag_list = [y for (x, y) in return_list]
        tag_list = [(y.lower()).title() for y in tag_list]

        # Zip input and tags
        temp_list = zip([t for t in sentence.split()], tag_list)

        return temp_list

    # Make the initiated class callable in the same way as a function
    def __call__(self, sentence):
        return list(self.tag(sentence))