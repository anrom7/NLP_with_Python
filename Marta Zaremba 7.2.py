# Marta Zaremba PRLs-11,
# Rozdil_7, Zadacha_2

import nltk, re, pprint
sentence = [("Many","JJ"), ("researchers","NNS"), ("developed","VBD "), ("both","DT"),
            ("new","JJ"), ("positions","NNS"), ("two","CD"), ("weeks","NNS"), ("ago","RB")]#create sentence
grammar = "NP: {<DT>*<CD>*<JJ>*<NN.*>+}" #create ragular expression
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
result = cp.parse(sentence)#test chunk parser on my sentence
print result #print result
