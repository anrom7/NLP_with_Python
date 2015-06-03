# Hanchevska Iryna, Chapter 7, Exercise 2

import nltk
#some sentence
sentence=[("many", "JJ"), ("researches", "NNS"), (",", ","), ("two", "CD"),
          ("weeks", "NNS"), (",", ","), ("both", "DT"),("new", "JJ"),
          ("position", "NNS")]
#define grammar with regular expression rule
grammar="NP:{<DT|CD>?<JJ>*<NN.>}"
#create a chunk parser with defined grammar
cp=nltk.RegexpParser(grammar)
#present result
result=cp.parse(sentence)
print result
result.draw()
