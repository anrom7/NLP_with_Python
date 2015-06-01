import nltk
# tokenize the input
tokens = 'you claim that you like cats'.split()
# after tokenizing the input, import the load_parser function, which takes a grammar filename as input and returns a chart parser cp
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat1.fcfg')
# display tree
for tree in cp.nbest_parse(tokens):
	print tree

# S -> N[BAR=2] V[BAR=2]
# N[BAR=2] -> Det N[BAR=1]
# N[BAR=1] -> N[BAR=1] P[BAR=2]
# N[BAR=1] -> N[BAR=0] P[BAR=2]




    
