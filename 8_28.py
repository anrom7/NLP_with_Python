# Chapter 8
# Exercise 28
# Author Svitlana Syytsia
'''
Process each tree of the Penn Treebank Corpus sample nltk.corpus.treebank
and extract the productions with the help of Tree.productions(). Discard the productions
that occur only once. Productions with the same lefthand side and similar
righthand sides can be collapsed, resulting in an equivalent but more compact set
of rules. Write code to output a compact grammar.
'''
import nltk
from nltk.corpus import treebank
l = treebank.parsed_sents()[:10]# list of 10 syntactically analyzes trees
allproductions = []# list for the rules
for tree in l:
    for p in tree.productions():
        allproductions.append(p)# adding of rules into the list


from nltk import FreqDist
fd=FreqDist(allproductions)
print fd.hapaxes()#print the rules that are used only once
