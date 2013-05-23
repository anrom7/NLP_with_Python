# julia vezdenko, AL-12 task 22 chapter 5 
import nltk
import pprint
from nltk import RegexpTagger, word_tokenize

patterns = [
# Created regular expressions
(r'(The|the|A|a|An|an)$', 'AT'), # articles
(r'(of|at|in|on|against)$', 'IN'), # prepositions
(r'.*ous$', 'JJ'), # adjectives
(r'.*ity$', 'NNJ'), # nouns formed from adjectives
(r'.*ly$', 'RB'), # adverbs
(r'.*self$|.*selves$', 'PRR'), # reflexive pronoun

# Regular expressions taken from this chapter
(r'.*ing$', 'VBG'), # gerunds
(r'.*ed$', 'VBD'), # simple past
(r'.*es$', 'VBZ'), # 3rd singular present
(r'.*ould$', 'MD'), # modals
(r'.*\'s$', 'NN$'), # possessive nouns
(r'.*s$', 'NNS'), # plural nouns
(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
(r'.*', 'NN'), # nouns (default)
]
regexp_tagger = RegexpTagger(patterns)
sentence = raw_input("Enter test sentence:\n")
pprint.pprint(regexp_tagger.tag(word_tokenize(sentence)))
# A test sentence to enter:
# The nomerous droughts in the region themselves strongly affected a scarcity of water.
