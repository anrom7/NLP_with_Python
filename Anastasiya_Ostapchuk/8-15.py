# Anastasiya Ostapchuk
# PRLs-12
# Chapter 8, Exercise 15
# TODO: Extend grammar in grammar2 with productions that expand prepositions
# as intransitive, transitive, and requiring a PP complement.

import nltk, re, pprint
# extending grammar
grammar2 = nltk.parse_cfg("""
    S -> NP VP
    NP -> Det Nom | PropN
    Nom -> Adj Nom | N
    VP -> V Adj | V NP | V S | PP NP | PP Nom | V PP NP
    PP -> V TP | IP
    PropN -> 'Buster' | 'Chatterer' | 'Joe' | 'Lee'
    Det -> 'the' | 'a'
    N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log' | 'home'
    Adj -> 'angry' | 'frightened' | 'little' | 'tall'
    V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put' | 'ran'
    IP -> 'to'
    TP -> 'away'
    """)

sent = ['Lee', 'ran', 'away', 'home']
# creating parser
parser = nltk.ChartParser(grammar2)
trees = parser.nbest_parse(sent)
# parsing two sntences
for tree in trees:
	print 'Sentence with TP: ', tree
	sent = ['Lee', 'said', 'to', 'Joe']
	parser = nltk.ChartParser(grammar2)
	trees = parser.nbest_parse(sent)
	for tree in trees:
		print 'Sentence with IP: ', tree
