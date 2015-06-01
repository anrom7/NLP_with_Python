#Turianska K., PrLs-11, Chapter_7_ex_3
# 3.1
import nltk
sentence = [("many", "JJ"), ("researches", "NNS"), (",", ","), ("two", "CD"), ("weeks", "NNS"), (",", ","), ("both", "DT"), ("new", "JJ"), ("positions", "NNS")]
grammar = r"NP:  {<DT|CD>?<JJ>*<NN.>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()

# -------------------------------------
# 3.2
import nltk
sentence = [("A", "DT"), ("dark", "JJ"), ("red", "JJ"), ("car", "NN"), ("came", "VBD"), ("to", "IN"), ("a", "DT"), ("stopt", "NN"), ("in", "IN"), ("front", "NN"), ("of", "IN"), ("the", "DT"), ("Flynn-Fletcher", "JJ"), ("residence", "NN"), ("that", "WDT"), ("same", "JJ"), ("evening", "NN"), (",", ","), ("in", "IN"), ("another", "DT"), ("demension", "NN"), (".", ".")]
grammar = r"NP:	{<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()
