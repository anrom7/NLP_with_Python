# Hanchevska Iryna, Chapter 9, Exercise 7
from nltk import load_parser #import the load_parser function , which takes a
#grammar filename as input
tokens = 'ich folge den Katze'.split() # tokenize the sentence
cp = load_parser('grammars/book_grammars/german.fcfg', trace=2) #returns a chart parser
#cp
trees = cp.nbest_parse(tokens) #Calling the parser’s nbest_parse() method
#will return a list trees of parse trees
