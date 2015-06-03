# Anna Hadzalo
#PRLS-11
#Chapter 5
# Task 9

import nltk
from nltk.corpus import brown
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if w2=='go':
            print t1, t3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if w2=='went':
            print t1, t3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)
#�������� � ����������� �����, �� ������ ��������� ����� 䳺������� go �� went, �� ���� ���.

sent1=nltk.word_tokenize("Go away!")
sent2=nltk.word_tokenize("We went on the excursion.")
nltk.pos_tag(sent1), nltk.pos_tag(sent2)
print nltk.pos_tag(sent1), nltk.pos_tag (sent2)

#���� � �������� ���������� ������, � ���� ���������� ��� 䳺�����.
#� ��������� � ������� ��������, �� 䳺����� go �� went ��������� ��� ��������� �����.
#���� ����� � ��� ��������� � ����������� ��������.
#� ������ ������� �������� ��� 䳺��� �������� �� ���������� ������� - ����.
