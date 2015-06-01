# Fedorchak V, Als-11

import nltk
grammar = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "notice" | "ask"
NP -> "Sarah" | "Jake" | "Johny" | Det N | Det N PP
Det -> "a" | "an" | "the" | "his"
N -> "book" | "noise" | "friend" | "room" | "computer"
P -> "at" | "in" | "about" | "with"
""")                             # Creating the grammar
rd_parser = nltk.RecursiveDescentParser(grammar) # Using the recursive descent parser
sent = 'Sarah notice a noise'.split() 
for w in rd_parser.nbest_parse(sent):
    print w
sent = 'Jake ask Johny'.split() 
for w in rd_parser.nbest_parse(sent):
    print w
sent = 'Johny notice a friend in the room'.split()
for w in rd_parser.nbest_parse(sent):
    print w
sent = 'Sarah notice Johny with his friend'.split() 
for w in rd_parser.nbest_parse(sent):
    print w
sent = 'Sarah notice Johny with his friend at the computer'.split() 
for w in rd_parser.nbest_parse(sent):
    print w
