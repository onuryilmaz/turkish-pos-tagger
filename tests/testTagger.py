# -*- coding: cp1254 -*-

# Onur Yilmaz
import os
import unittest
import tempfile
import shutil
from nltk.tag.brill import BrillTagger

from Tagger import Tagger

class TestTaggerSetUp(unittest.TestCase):
    def setUp(self):
        self.tempDir = tempfile.mkdtemp()
        self.filePath = 'my_tagger.yaml'

    def test_load_file(self):
        tagger = Tagger.load(self.filePath)
        self.assertIsInstance(tagger.myTagger, BrillTagger)

    def test_load_nonexisting(self):
        with self.assertRaises(FileNotFoundError):
            Tagger.load("this_file_definitely_doesnt_exist.txt")

    def test_load_incorrectly(self):
        temporaryFileName = os.path.join(self.tempDir, 'temporary_file.txt')
        with open(temporaryFileName, 'w') as file:
            file.write("This is a line that won't be able to be read")
        with self.assertRaises(TypeError):
            Tagger.load(temporaryFileName)

    def tearDown(self):
        shutil.rmtree(self.tempDir)

class TestTagger(unittest.TestCase):
    def setUp(self):
        self.filePath = 'my_tagger.yaml'
        self.tag = Tagger.load(self.filePath)

    def test_extract_using_tag(self):
        exampleText = "Babası papazdı, ama bitkilere ve ziraata karşı ilgi duyuyordu"
        result = [('Babası', 'Noun_Nom'),
                    ('papazdı,', 'Noun_Nom'),
                    ('ama', 'Conj'),
                    ('bitkilere', 'Noun_Nom'),
                    ('ve', 'Conj'),
                    ('ziraata', 'Noun_Nom'),
                    ('karşı', 'Adj'),
                    ('ilgi', 'Noun_Nom'),
                    ('duyuyordu', 'Verb')]
        resultZip = zip((item[0] for item in result), (item[1] for item in result))
        extractedResult = self.tag.tag(exampleText)
        self.assertIsInstance(resultZip, zip)
        self.assertListEqual(list(resultZip), list(extractedResult))

    def test_extract_using_text(self):
        exampleText = "Babası papazdı, ama bitkilere ve ziraata karşı ilgi duyuyordu"
        result = [('Babası', 'Noun_Nom'),
                  ('papazdı,', 'Noun_Nom'),
                  ('ama', 'Conj'),
                  ('bitkilere', 'Noun_Nom'),
                  ('ve', 'Conj'),
                  ('ziraata', 'Noun_Nom'),
                  ('karşı', 'Adj'),
                  ('ilgi', 'Noun_Nom'),
                  ('duyuyordu', 'Verb')]
        extractedResult = self.tag(exampleText)
        self.assertListEqual(extractedResult, result)

    def test_extract_input_error(self):
        exampleText = ['a', 'list', 'of', 'things']
        with self.assertRaises(TypeError):
            self.tag.tag(exampleText)