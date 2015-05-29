# Chapter 7
# Exercise 6
# Author Svitlana Synytsia
'''
Write one or more tag patterns to handle coordinated noun phrases, e.g., July/
NNP and/CC August/NNP, all/DT your/PRP$ managers/NNS and/CC supervisors/NNS,
company/NN courts/NNS and/CC adjudicators/NNS.
'''

import nltk
sentence = [("July", "NNP"), ("and", "CC"), ("August", "NNP"), ("all", "DT"), ("your", "PRP$"),
            ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"), ("company", "NN"),
            ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")] #Sentence that should be chunked.
grammar = "NP:{<DT|PRP\$|NN.*>+<CC><NN.*>+}" #Define a grammar with the regular expression rules
chunk_parser=nltk.RegexpParser(grammar) #Create a chunk parser
print chunk_parser.parse(sentence) #The result is a tree, which we can print
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus. The corpus contains 270k words of 
                                  #Wall Street Journal text, divided into “train” and “test” portions, annotated with 
				                  #part-of-speech tags and chunk tags in the IOB format.
test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=['NP']) #We are interested in the NP chunks right now.  
                                                                       #So we can use the chunk_types argument to select them.
print chunk_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
