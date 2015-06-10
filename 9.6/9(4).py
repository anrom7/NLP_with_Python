illustraiting the grammar with a BAR feature for dealing with phrasal projections.

#The grammar feat1.fcfg contains one “gap-introduction” production,
#namely S[-INV] -> NP S/NP. In order to percolate the slash feature correctly,
#we need to add slashes with variable values to both sides of the arrow in productions
#that expand S, VP, andNP. For example, VP/?x -> V SBar/?x is the slashed version
#of VP -> V SBar and says that a slash value can be specified on the VP parent
#of a constituent if the same value is also specified on the SBar child.

tokens = 'who do you claim that you like'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree
    tree.draw()


