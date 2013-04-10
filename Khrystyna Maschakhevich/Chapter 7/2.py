##Khrystyna Maschakhevich, AL-13, Chapter 7, Task 2. The tast was write a tag for nouns
## This program shows tags and diagram
 import nltk

sentence=[("many", "JJ"), ("researches", "NNS"), (",", ","), ("two", "CD"), ("weeks", "NNS"), (",", ","), ("both", "DT"),("new", "JJ"), ("position", "NNS")]
##sentence
grammar="NP:{<DT|CD>?<JJ>*<NN.>}" ## grammar with regular expression rule
cp=nltk.RegexpParser(grammar)## using that grammar we create a chunk parser
result=cp.parse(sentence)## results

## one can look at results with the help of -print result
## one can draw a diagram with the help of - result.draw()
