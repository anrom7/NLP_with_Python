# Shepelevych / PRLs-11

import nltk
from nltk.corpus import treebank #import corpus treebank
tree = treebank.parsed_sents('wsj_0005.mrg')[1] #отримуємо доступ до синтаксично розміченого речення
print 'Tree = ', tree #виводимо речення у вигляді дерева
tree.productions() #виписуємо всі правила з цього дерева
freqdist = nltk.FreqDist(tree.productions()) 
freqdist.keys() #формуємо список правил
print '  Grammar = '
for i in freqdist.keys():
	if freqdist[i]>=1:
		print '          ', i
		
