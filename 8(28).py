#chapter 8, Ex. 28
#by Ivanna Rurych
#task: Process each tree of the Penn Treebank Corpus sample  nltk.corpus.treebank
#and extract the productions with the help of Tree.productions(). Discard the productions that occur only once. Productions with the same lefthand side and similar
#righthand sides can be collapsed, resulting in an equivalent but more compact set
#of rules. Write code to output a compact grammar.
import nltk
from nltk.corpus import treebank 
tree = treebank.parsed_sents('wsj_0004.mrg')[2] 
print 'Tree = ', tree #One of the trees of the Penn Treebank Corpus 
tree.productions() 
freqdist = nltk.FreqDist(tree.productions())
print freqdist.keys()
print ' Grammar = ' #Print a grammar
for i in freqdist.keys():
    if freqdist[i]>= 1:
        print ' ', i

