# Anastasiya Ostapchuk
# PRLs-12
# Chapter 5, Exercise 22
# TODO: Create a regular expression tagger that tests for at least five new patterns in the spelling of words.

import nltk
import pprint
from nltk import RegexpTagger, word_tokenize
patterns = [
# Created regular expressions
(r'(The|the|A|a|An|an)$', 'DET'), # articles
(r'(of|at|in|on|against|about|for)$', 'P'), # prepositions
(r'(to|To)$', 'TO'), # preposition 'to'
(r'.*ous$', 'ADJ'), # adjectives
(r'(I|You|He|She|It|We|They|you|he|she|it|we|they)$', 'PRO'), # pronouns
(r'.*ly$', 'ADV'), # adverbs
(r'[.|!|?|,|(|)|;|:]$', 'PUN'), # punctuation

# Regular expressions taken from this chapter
(r'.*ing$', 'VBG'), # gerunds
(r'.*ed$', 'VBD'), # simple past
(r'.*es$', 'VBZ'), # 3rd singular present
(r'.*ould$', 'MOD'), # modals
(r'.*s$', 'NNS'), # plural nouns
(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
(r'.*', 'NN'), # nouns (default)
]
regexp_tagger = RegexpTagger(patterns)
sentence = raw_input("Enter test sentence:\n")
pprint.pprint(regexp_tagger.tag(word_tokenize(sentence)))
# A test sentence to enter:
# Accordingly to the letters, he would question you about visiting lessons.
