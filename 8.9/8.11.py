import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""") # Creating the context-free grammar
sent = "John saw Mary".split()
rd_parser = nltk.RecursiveDescentParser(grammar1) # Parsing the sentence
for tree in rd_parser.nbest_parse(sent):
    print tree
nltk.app.rdparser() # Parsing the sentence with ShiftReduceParser
sr_parse = nltk.ShiftReduceParser(grammar1)
sent = 'Mary saw a dog'.split()
print sr_parse.parse(sent)
nltk.app.srparser()
