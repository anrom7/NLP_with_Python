import nltk
from nltk.corpus import treebank 
tree = treebank.parsed_sents('wsj_0001.mrg')[1] #creating tree
print tree
tree.productions()
freqdist = nltk.FreqDist(tree.productions()) 
freqdist.keys()
print 'Grammar'
for i in freqdist.keys(): #creating grammar
	if freqdist[i]>=1:
		print i
