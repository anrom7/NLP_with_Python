#”л€на ўомак ѕ–Ћс-12 

import nltk
from nltk.corpus import treebank                #≥мпортуЇмо corpus treebank
tree = treebank.parsed_sents('wsj_0005.mrg')[1] #отримуЇмо доступ до синтаксично розм≥ченого реченн€
print 'Tree = ', tree                           #виводмо реченн€ у вигл€д≥ дерева
tree.productions()                              #виписуЇмо вс≥ правила з цього дерева
freqdist = nltk.FreqDist(tree.productions()) 
freqdist.keys()                                 #формуЇмо список правил
print '  Grammar = '
for i in freqdist.keys():
	if freqdist[i]>=1:
		print '          ', i
		
