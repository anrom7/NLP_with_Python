#Turianska K. PrLs-11
#Chapter_5_ex_19

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

list_input = [
  (r'.*ing$', 'VBG'),               # gerunds
	(r'.*ed$', 'VBD'),                # past simple
	(r'.*es$', 'VBZ'),                # present simple(pers_3rd_sing)
	(r'.*ould$', 'MD'),               # modal verbs
	(r'.*\'s$', 'NN$'),               # possessive nouns
	(r'.*s$', 'NNS'),                 # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
	(r'.*', 'NN')                     # nouns (default)
]

t = nltk.RegexpTagger(list_input)
t.tag(brown_sents[2])
print "\nWait some seconds... Counting...\n"
print t.evaluate(brown_tagged_sents)
