# Taradakha K 7_8
import nltk
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus.
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NN'])
print cp.evaluate(test_sents)
#The IOB tag accuracy indicates that 100 of the words are tagged with 0.
#Its precision, recall, and F-measure are zero.
grammar = r"""
PP:
{<.*>+}                       
}<VBD|IN.>+{
"""  #{<.*>+} - Chunk everything. }<VBD|IN.>+{ - Chink sequences of VBD and IN
sentence= [("The", "DT"),("little", "JJ"),("yellow", "JJ"),("dog", "NN"),("barked", "VBD"),("at", "IN"),
           ("the", "DT"),("cat", "NN")] #Sentence that should be chunked.
chunk_parser=nltk.RegexpParser(grammar) #Creation of chunk parser
print chunk_parser.parse(sentence) #Test chunk_parser on our sentence.
chunk_parser = nltk.RegexpParser(grammar)#create a chunk parser once more
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NN'])
print chunk_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
                                        
