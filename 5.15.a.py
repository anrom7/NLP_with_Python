import nltk
from nltk.corpus import brown
sing=[]
pl=[]
for (w,t) in brown.tagged_words(categories='news'): # ³��� ��� �� ����� ��� �������� � �����.
	if t=='NN':
		sing.append(w)

fdistsing = nltk.FreqDist(sing) # ��������� ���������� ������ ������������ ���

for (w,t) in brown.tagged_words(categories='news'): # ³��� ��� �� ����� ��� �������� � ������ � ��������� � ������ ��� �������� �����
	if t=='NNS':
		pl.append(w[:-1])

fdistpl = nltk.FreqDist(pl) # ��������� ���������� ������ ������������ ���

for i in fdistpl.keys():	# ��������� ������� ��������� � ������ ��������. ���� ������� ��������� ����� � ������ �� � ����� �� ���������� ���� �� ����� ����� �����.
	if fdistpl[i]>fdistsing[i]:
		print i
