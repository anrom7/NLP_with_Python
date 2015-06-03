import nltk
from nltk.corpus import treebank
# Selecting Treebunk corpus.
tree = treebank.parsed_sents()[2]
# Choosing sentence. The number can be changed manualy.
print 'Sentence:'
print tree
tree.productions() 
freqdist = nltk.FreqDist(tree.productions()) 
freqdist.keys()
# Extracting productions.
for i in freqdist.keys():
 if freqdist[i]>=1:
  print i
# As the result, we can process each tree buy selecting it.
		
