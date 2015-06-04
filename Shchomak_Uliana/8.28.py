#����� ����� ����-12 

import nltk
from nltk.corpus import treebank                #��������� corpus treebank
tree = treebank.parsed_sents('wsj_0005.mrg')[1] #�������� ������ �� ����������� ���������� �������
print 'Tree = ', tree                           #������� ������� � ������ ������
tree.productions()                              #�������� �� ������� � ����� ������
freqdist = nltk.FreqDist(tree.productions()) 
freqdist.keys()                                 #������� ������ ������
print '  Grammar = '
for i in freqdist.keys():
	if freqdist[i]>=1:
		print '          ', i
		
