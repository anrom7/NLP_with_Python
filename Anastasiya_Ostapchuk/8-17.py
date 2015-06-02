# Anastasiya Ostapchuk
# PRLs-12
# Chapter 8, Exercise 17
# TODO: The program compares the efficiency of top-down chart parser
# and descent parser.

import nltk
# defining grammar
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

sent1 = "John ate Mary".split()
# creating top-down parser
rd_parser = nltk.RecursiveDescentParser(grammar1)
print rd_parser.parse(sent1)
