# Taradakha Kateryna 7_2

import nltk, re, pprint
sentence=[('He', 'PRP'), ('has', 'VBZ'), ('done', 'VBN'), ('many', 'JJ'), ('researches', 'NNS'), ('during', 'IN'), ('two', 'CD'), ('weeks', 'NNS'), ('by', 'IN'), ('working', 'VBG'), ('on', 'IN'), ('both', 'DT'), ('new', 'JJ'), ('positions', 'NNS')]

grammar="NP:{<DT>?<JJ|CD>*<NNS>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
