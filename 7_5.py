### Chapter 7 task 5


import nltk
from nltk.corpus import conll2000
"""
create a pattern
"""
grammar = "NP: {<VBG><NN.*>?<IN><DT>?<NN>}"
cp = nltk.RegexpParser(grammar)
"""
My sample
"""
sent = 'Sharing book with student'
sent = sent.split()
tagd = nltk.pos_tag(sent)
result = cp.parse(tagd)
print (result)
