# Iryna Kupyak, PRLs-12, Chapter 8, exercise 20
# The task was to compare multiple trees in a single window
import nltk
from nltk import tree
from nltk.draw.tree import draw_trees
grammar1=nltk.parse_cfg("""
    S -> NP VP
    NP -> Det N
    VP -> VP AP | V NP
    AP -> Adj PropN
    Det -> 'a' | 'The'
    N -> 'police' | 'child'
    V -> 'saved'
    Adj -> 'previous'
    PropN -> 'Monday'
    """)
#grammar for first sent.

sent=['The', 'police', 'saved', 'a', 'child', 'previous', 'Monday']
parser = nltk.ChartParser(grammar1)
tree1 = parser.nbest_parse(sent)
grammar2 = nltk.parse_cfg("""
    S -> NP
    NP -> Adj NP
    NP -> N Conj N
    Conj -> 'and'
    N -> 'police' | 'child'
    Adj -> 'noisy'
    """)
#grammar for second sent.
parser2 = nltk.ChartParser(grammar2)
sent2=['noisy', 'police', 'and', 'child']
tree2 = parser2.nbest_parse(sent2)
draw_trees(tree1, tree2)

# to draw the trees one have to use -draw_trees(tree1, tree2)
