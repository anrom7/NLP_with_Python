### Chapter 8 task 13

import nltk
from nltk import tree
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> NP RC
    RC -> NP V
    NP -> PN N
    VP -> V NP
    PN -> 'Buffalo'
    N -> 'buffalo'
    V -> 'buffalo'
    """)
parser = nltk.ChartParser(grammar)
sent=['Buffalo', 'buffalo', 'Buffalo', 'buffalo', 'buffalo', 'buffalo', 'Buffalo', 'buffalo']
trees = parser.parse(sent)
for tree in trees:
    print(tree)
