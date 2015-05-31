# Shepelevych, PRLs-11
#The grammar feat1.fcfg contains one “gap-introduction” production,
#namely S[-INV] -> NP S/NP. In order to percolate the slash feature correctly,
#we need to add slashes with variable values to both sides of the arrow in productions
#that expand S, VP, andNP. 
tokens = 'whom do you want to kill'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree
    tree.draw()
