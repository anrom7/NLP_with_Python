import nltk
fs1=nltk.FeatStruct(TENSE='past', NUM='sg')
fs2=nltk.FeatStruct(TENSE='past', NUM='sg', GND='fem', ARG=fs1)
print fs1
print fs2
print fs1.subsumes (fs2) #���������� �� fs1 ������ � ��� fs2
print fs2.subsumes (fs1) #���������� �� fs2 ������ � ��� fs1
# � ��� ������� �� ������ �� ���������,��� ���� � �������, ���� fs1 ������ � ���� fs2
def subs (fs1, fs2):
	if fs1.subsumes (fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes (fs1):
		print fs2.unify(fs1)
	else: print "None"
