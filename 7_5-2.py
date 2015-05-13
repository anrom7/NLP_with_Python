### Chapter 7 task 5
# 2 variant vidpovidi

import nltk
from nltk.corpus import conll2000
sent = [("sharing", "VBG"), ("book", "NN"), ("with", "IN"), ("student", "NN")]
grammar = "NP: {<VBG><NN.*>?<IN><DT>?<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sent)
print (result)
