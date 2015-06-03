# Iryna Kupyak, Chapter 7, Exercise 3

import nltk
from nltk.corpus import conll2000
grammar="NP: {<DT|JJ>?<RB>?<VBN>?<NN.*>+}" 
sent='Either way, I very much doubt that writing schools give any space to the idea that there are some passages in great novels that are so profoundly boring they should not detain our attention.'
sentence=sent.split() # devided sentence into single words
tagged=nltk.pos_tag(sentence) #tagged the words
cp=nltk.RegexpParser(grammar) # developed a simple chunker
result=cp.parse(tagged)
print result
