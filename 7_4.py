# Anna Karbivska, ALs-11
# 7.9.4
# An early definition of chunk was the material that occurs between chinks. Develop
#a chunker that starts by putting the whole sentence in a single chunk, and
#then does the rest of its work solely by chinking. Determine which tags (or tag
#sequences) are most likely to make up chinks with the help of your own utility
#program. Compare the performance and simplicity of this approach relative to a
#chunker based entirely on chunk rules.

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
