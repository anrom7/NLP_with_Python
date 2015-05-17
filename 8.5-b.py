### Chapter 8 task 5

#VARIANT I-b

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
#(S (NP (Adj old) (NP (N man) (Conj and) (N woman))))

t1 = nltk.Tree('Adj', ['old'])
t2 = nltk.Tree('N', ['man'])
t3 = nltk.Tree('N', ['woman'])
t4 = nltk.Tree('Conj', ['and'])
t5 = nltk.Tree('NP', ['man', 'and', 'woman'])
t = nltk.Tree('S', [t1, t5])
t.draw()
