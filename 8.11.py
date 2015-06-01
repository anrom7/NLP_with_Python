import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "chopped"
NP -> "Arthur" | Det N | Det N PP
Det -> "a" | "an" | "the" | 
N -> "forest" | "tree" | "axe" 
P -> "in" | "with"
""") #Write a simple context-free grammar.
sent = "Arthur chopped a tree with an axe in the forest".split() #Sentence that should be parsed
rd_parser = nltk.RecursiveDescentParser(grammar1) #Call the recursive descent parser
for tree in rd_parser.nbest_parse(sent):
    print tree  #Parse the sentence with the recursive descent parser
sent = "Arthur chopped a tree with an axe".split() #Sentence that should be parsed
sr_parse = nltk.ShiftReduceParser(grammar1) #Call the 
print sr_parse.parse(sent)#Print the sentence parsed with shift-reduce parser
#Recursive descent parsing is a kind of top-down parsing. Top-down parsers use a
#grammar to predict what the input will be, before inspecting the input.
#Shift-reduce parser is a kind of bottom-up parser. A shift-reduce parser tries to find sequences 
#of words and phrases that correspond to the righthand side of a grammar production, and replace
#them with the lefthand side, until the whole sentence is reduced to an S.
