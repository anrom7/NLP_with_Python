# Anastasiya Ostapchuk
# PRLs-12
# Chapter 8, Exercise 20
# TODO: Compare multiple trees in a single window.

import nltk
from nltk import tree
from nltk.draw.tree import draw_trees
# defining grammar for the 1st sentence
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
# creating parser for the 1st sentence
sent=['The', 'police', 'saved', 'a', 'child', 'previous', 'Monday']
parser = nltk.ChartParser(grammar1)
tree1 = parser.nbest_parse(sent)
# defining grammar for the 2nd sentence
grammar2 = nltk.parse_cfg("""
    S -> NP
    NP -> Adj NP
    NP -> N Conj N
    Conj -> 'and'
    N -> 'police' | 'child'
    Adj -> 'noisy'
    """)
# creating parser for the 2nd sentence
parser2 = nltk.ChartParser(grammar2)
sent2=['noisy', 'police', 'and', 'child']
tree2 = parser2.nbest_parse(sent2)

draw_trees(tree1, tree2)
