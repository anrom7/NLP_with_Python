import nltk
from nltk.corpus import treebank 
tree = treebank.parsed_sents('wsj_0004.mrg')[2] 
print 'Tree = ', tree #One of the trees of the Penn Treebank Corpus 
tree.productions() 
freqdist = nltk.FreqDist(tree.productions())
print freqdist.keys()
print ' Grammar = ' #Print a grammar, but not compact
for i in freqdist.keys():
    if freqdist[i]>= 1:
        print ' ', i

