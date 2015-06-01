import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "buy" | "saw" | "draw" | "failed"|"asked"
NP -> "Kim" | "Katy" | "Tom" | "Mark" | "Lina" | Det N | Det N PP
Det -> "a" | "an" | "the" | 
N -> "doll" | "bird" | "tree" | "house" | "board" | "exam" | "shame" | "help" 
P -> "in" | "with" | "on"
""") #Write a simple context-free grammar.
sent1 = "Kim buy a doll".split()
sent2 = "Katy saw a bird on the tree".split()
sent3 = "Tom draw a house on the board".split()
sent4 = "Mark failed an exam with a shame".split()
sent5 = "Lina asked a help".split()
rd_parser = nltk.RecursiveDescentParser(grammar1) #Call the recursive descent parser
for tree in rd_parser.nbest_parse(sent1): #Parse the sentences 1-5
	print tree	
for tree in rd_parser.nbest_parse(sent2):
	print tree	
for tree in rd_parser.nbest_parse(sent3):
	print tree	
for tree in rd_parser.nbest_parse(sent4):
	print tree
for tree in rd_parser.nbest_parse(sent5):
	print tree
nltk.app.rdparser()
 
