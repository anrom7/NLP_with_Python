
import nltk
from nltk.corpus import brown
words_brown=brown.tagged_words() 
tags_brown=[t for w,t in words_brown] # �������� ����� ���� ������� Brown �� ����� ��������� �����
fd=nltk.FreqDist(tags_brown)
print fd.items()[:10] 
