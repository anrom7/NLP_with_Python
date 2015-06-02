# Anastasiya Ostapchuk
# PRLs-12
# Chapter 7, Exercise 8
# TODO: Develop a chunker for one of the chunk types in the CoNLL Chunking Corpus
# using a regular expression- based chunk grammar

import nltk
from nltk.corpus import conll2000
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NN'])
print cp.evaluate(test_sents)
# the IOB tag accuracy indicates that 100 of the words are tagged with 0
# its precision, recall, and F-measure are zero

grammar = r"""
NP:
{<.*>+}                       
}<VBD|IN>+{
"""
# {<.*>+} - chunk everything
# }<VBD|IN>+{ - chink sequences of VBD and IN

# sentence that should be chunked
sentence= [("The", "DT"),("little", "JJ"),("happy", "JJ"),("boy", "NN"),("jumped", "VBD"),("on", "IN"),
           ("the", "DT"),("bed", "NN")]
# creating chunk parser
chunk_parser=nltk.RegexpParser(grammar)
# testing chunk_parser on the sentence
print chunk_parser.parse(sentence)
# creating a chunk parser once more
chunk_parser = nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NN'])
# evaluating chunker on the data for testing
print chunk_parser.evaluate(test_sents)

