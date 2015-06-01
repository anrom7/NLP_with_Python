import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "watched" | "saw" | "walked" | "chopped"
NP -> "John" | "Jane" | "Bob" | "Michael" | "Arthur" | Det N | Det N PP
Det -> "a" | "an" | "the" | 
N -> "film" | "dog" | "street" | "park" | "book" | "cat" | "tree" | "wood" | "axe" 
P -> "in" | "with" | "on"
""") #Write a simple context-free grammar.
sent1 = "John watched a film".split()
sent2 = "Jane saw a dog on the street".split()
sent3 = "Bob saw John with a book in the park".split()
sent4 = "Michael saw a cat in a tree".split()
sent5 = "Arthur chopped a tree with an axe".split()
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
#I have experimented with changing the sentence to be parsed. As you can see for one
#sentence several trees were built. I called a recursive descent parser - nltk.app.rdparser()
#and changed the sentence to be parsed by selecting Edit Text in the Edit menu. But I noticed
#that the changed sentence couldn't be parsed because the Grammar corresponded to a different sentence.
#So, it is necessary to change the grammar that corresponds to my sentence. 
