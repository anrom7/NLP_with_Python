# Pushchinska_Iryna PRLs-11
# Chapter_5, Task_3

import nltk
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind.")
nltk.pos_tag(text)
print nltk.pos_tag(text)
#POS tagger ��������� ����������� ��� � �������� ������� ����� ��� ������� ����. ���������� �������� ��������, �� ����� 'They' - ���������, 'wind'-䳺�����, 'back'-���������, 'the'-�������, 'clock'-��������, 'while'-���������, 'we'-���������, 'chase'-䳺�����, 'after'-���������, 'the'-�������, 'wind'- �������.   
#��� ����� �� ��� ������� ���� �������� �����. ��������� ����� wind ���������� 2 ����, ������ ��� ���� ������� 䳺������ � ������ "���������� �����", � ������-��������� - "����".
