# Hanchevska Iryna, Chapter 9, Exercise 5
import nltk
from nltk import load_parser   # the load_parser function which takes a grammar filename as input and returns a chart parser cp
tokens = 'ich folge den Katzen'.split() # a sentence
cp = load_parser('grammars/book_grammars/german.fcfg') # return a list trees of parse trees
for tree in cp.nbest_parse(tokens):
	print tree                                  #print our tree




from nltk import load_parser
tokens = 'die Katze hilft dem Hund '.split()
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree

tokens = 'du kommst '.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.nbest_parse(tokens):
	print tree
