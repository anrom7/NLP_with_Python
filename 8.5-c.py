### Chapter 8 task 5-c


import nltk
from nltk import tree
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> DT N
    VP -> VBD NP AP
    AP -> Adj N
    N -> 'woman' | 'man' | 'Thursday'
    DT -> 'The' | 'a'
    Adj -> 'last'
    VBD -> 'saw'
    """)
parser = nltk.ChartParser(grammar)
sent = ['The', 'woman', 'saw', 'a', 'man', 'last', 'Thursday']
trees = parser.parse(sent)
for tree in trees:
	print (tree)
tree.draw()
