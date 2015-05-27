import nltk, re, pprint
grammar2 = nltk.CFG.fromstring("""
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
IP -> 'on'
TP -> 'away'
""")
sent = ['Lee', 'ran', 'away', 'home']
parser = nltk.ChartParser(grammar2)
trees = parser.parse(sent)
for tree in trees:
	print (tree)
