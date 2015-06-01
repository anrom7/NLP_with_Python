# Marta Zaremba PRLs-11
# Rozdil_7, Zadacha_4 

import nltk

grammar = r""" 
  NP: 
     {<.*>+}             # Chunk everything 
     }<VB.|IN>+{         # Chink sequences of VB and IN 
  """
sentence =[("The", "DT"), ("tall", "JJ"), ("nice", "JJ"),
       ("girl", "NN"), ("walked", "VBD"), ("to", "IN"),  ("the", "DT"), ("cinema", "NN")]
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result #print result
from nltk.corpus import conll2000 #import conll2000 corpus for making evaluation
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=('NP',))
print cp.evaluate(test_sents) #print evaluation
