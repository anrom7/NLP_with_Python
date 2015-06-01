# Anna Karbivska Als-11
# 9.6.6
# Develop a feature-based grammar that will correctly describe the following
#Spanish noun phrases.

import nltk
from nltk import load_parser  # the load_parser function which takes a grammar filename as input and returns a chart parser cp
token1 = 'un cuadro hermoso'.split() # spanish phrases
token2 = 'unos cuadros hermosos'.split()
token3 = 'una cortina hermosa'.split()
token4 = 'unas cortinas hermosas'.split()
cp = load_parser('grammars/book_grammars/spanish_new.fcfg', trace=2) #return a list trees of parse trees
tree1 = cp.nbest_parse(token1)
tree2 = cp.nbest_parse(token2)
tree3 = cp.nbest_parse(token3)
tree4 = cp.nbest_parse(token4)
print tree1
print tree2
print tree3
print tree4
