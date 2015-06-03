# Hanchevska Iryna, Chapter 8, Exercise 17

# The program comoares the efficiency of top-down chart parser and descent parser.
# Timeit module compares their performance
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
#define grammar
sent1 = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
print rd_parser.parse(sent1)

