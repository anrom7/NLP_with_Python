import nltk
grammar = nltk.CFG.fromstring("""
    S -> VP NAP
    VP -> Pron V
    NAP -> NP Adv
    NP -> Det N
    V -> 'saw'
    Pron -> 'I'
    Det -> 'a'
    N -> 'cat'
    Adv -> 'yesterday'
    """)
rd_parser = nltk.RecursiveDescentParser(grammar)
sent = 'I saw a cat yesterday'.split()
for t in rd_parser.parse(sent):
    t.draw()
td_parser = nltk.TopDownChartParser(grammar)
sent = 'I saw a cat yesterday'.split()
for tree in rd_parser.parse(sent):
    print (tree)
