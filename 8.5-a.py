### Chapter 8 task 5

#VARIANT I

import nltk
from nltk import tree
grammar1 = nltk.CFG.fromstring("""
    S -> Adj NP
    NP -> N Conj N
    Conj -> 'and'
    N -> 'woman' | 'man'
    Adj -> 'old'
    """)
parser = nltk.ChartParser(grammar1)
sent=['old', 'man', 'and', 'woman']
trees = parser.parse(sent)
for tree in trees:
	print (tree)

#VARIANT II
	
import nltk
from nltk import tree
grammar2 = nltk.CFG.fromstring("""
    S -> NP
    NP -> ANP Conj N
    ANP -> Adj N
    Conj -> 'and'
    N -> 'woman' | 'man'
    Adj -> 'old'
    """)
parser = nltk.ChartParser(grammar2)
sent=['old', 'man', 'and', 'woman']
trees = parser.parse(sent)
for tree in trees:
	print (tree)
