# Chapter 8
# Exercise 19
# Author Svitlana Synytsia
'''
Read up on “garden path” sentences. How might the computational work of a
parser relate to the difficulty humans have with processing these sentences? (See
http://en.wikipedia.org/wiki/Garden_path_sentence.)
'''
import nltk
# define the grammar
groucho_grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N VP 
VP -> V PP | V
Det -> 'The' | 'the'
N -> 'horse' | 'barn'
V -> 'raced' | 'fell'
P -> 'past'
""")
# define our sentence
sent = ['The', 'horse', 'raced', 'past', 'the', 'barn', 'fell']
# analyze our grammar using ChartParser
parser = nltk.ChartParser(groucho_grammar)
trees = parser.nbest_parse(sent)
# display results
for tree in trees:
	print tree
# rechennja garden path e vagki dlja rozyminnja Y nashomy vupadky bachumo wo pershe derevo pravulno zbydovane, a dryhe - ni.
