# Iryna Kupyak, Chapter 7, Exercise 5

import nltk
from nltk.corpus import conll2000
grammar="NP: {<DT|NN>?<VBG>?<DT|NN.*>+}" 
cp=nltk.RegexpParser(grammar) # chunker
sentence="After wreaking havoc in global financial markets last year, the debt crisis in Europe has entered a complicated new phase in 2012."
sentence=sentence.split() # devided sentence into single words
tagged=nltk.pos_tag(sentence) #tagged the words
result=cp.parse(tagged)
print result


