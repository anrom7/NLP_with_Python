#Chapter 9
#Exercise 5
#Author Sofiya Zaliska ALs-11
#Modify the German grammar in Example 9-4 to incorporate the treatment of
#subcategorization presented in Section 9.3.
import nltk
from nltk import load_parser   # load_parser function which takes a grammar filename as input and returns a chart parser cp
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
# So with the help of this program we can also work with different words in German.
# we can check parson, number and gender, which are difficult in this language.
# we can put the rules in a file where they can be edited, tested and revised.
