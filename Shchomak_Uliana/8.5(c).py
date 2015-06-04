
# Уляна Щомак ПРЛс-12 

import nltk
from nltk import tree # Створюю контекстно вільну граматику
groucho_grammar = nltk.parse_cfg("""
    S -> NP VP
    NP -> Det N
    VP -> VP AP | V NP
    AP -> Adj PropN
    Det -> 'a' | 'The'
    N -> 'woman' | 'man'
    V -> 'saw'
    Adj -> 'last'
    PropN -> 'Thursday'
    """)
sent=['The', 'woman', 'saw', 'a', 'man', 'last', 'Thursday']
parser = nltk.ChartParser(groucho_grammar)# Парсер на основі створеної граматики
trees = parser.nbest_parse(sent) # Побудова дерева
for tree in trees:
	print tree

#(S
#  (NP (Det The) (N woman))
#  (VP
#    (VP (V saw) (NP (Det a) (N man)))
#    (AP (Adj last) (PropN Thursday))))

for tree in trees:
	tree.draw()
