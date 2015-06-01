import nltk
sentence=[("many", "JJ"), ("researches", "NNS"), (",", ","), ("two", "CD"), ("weeks", "NNS"), (",", ","), ("both", "DT"),("new", "JJ"), ("position", "NNS")]
grammar="NP:{<DT|CD>?<JJ>*<NN.>}" # grammar with regular expression rule
cp=nltk.RegexpParser(grammar)     # using that grammar we create a chunk parser
result=cp.parse(sentence)         # results
