#presented by Volkov Mark PRLc 11
# Chapter 8, Ex.9
"""
Possibly, but if the sentence will contain only the words that are written in the grammar, otherwise we get an error. 
"""
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
""")
sent = "Mary walked in the park with a dog and saw Bob with a cat".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
	print tree
