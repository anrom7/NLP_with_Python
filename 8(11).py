#chapter 8, Ex. 11
#by Ivanna Rurych
#task: With pen and paper, manually trace the execution of a recursive descent parser
#and a shift-reduce parser, for a CFG you have already seen, or one of your own
#devising
import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "chopped"
NP -> "Ann" | Det N | Det N PP
Det -> "a" | "an" | "the" | 
N -> "forest" | "five" | "axe" 
P -> "in" | "with"
""") #Write a simple context-free grammar.
sent = "Ann chopped a five with an axe in the forest".split() #Sentence that should be parsed
rd_parser = nltk.RecursiveDescentParser(grammar1) #Call the recursive descent parser
for tree in rd_parser.nbest_parse(sent):
    print tree  #Parse the sentence with the recursive descent parser
sent = "Ann chopped a five with an axe".split() #Sentence that should be parsed
sr_parse = nltk.ShiftReduceParser(grammar1) #Call the 
print sr_parse.parse(sent)#Print the sentence parsed with shift-reduce parser

