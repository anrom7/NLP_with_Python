import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

list_input = [
  (r'.*ing$', 'VBG'),               # gerunds
	(r'.*ed$', 'VBD'),                # simple past
	(r'.*es$', 'VBZ'),                # 3rd singular present
	(r'.*ould$', 'MD'),               # modals
	(r'.*\'s$', 'NN$'),               # possessive nouns
	(r'.*s$', 'NNS'),                 # plural nouns
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
	(r'.*', 'NN')                     # nouns (default)
]

t = nltk.RegexpTagger(list_input)
t.tag(brown_sents[2])
print "\nWait some seconds... Counting...\n"
print t.evaluate(brown_tagged_sents)
#We can improve the performance this number by improving 
#	RegExr or/and combine this tagger with the default tagger
