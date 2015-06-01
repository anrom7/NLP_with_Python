# TODO
#In Table 3-1, we saw a table involving frequency counts for the verbs adore,
#love,like, and prefer, and preceding qualifiers such as really. Investigate
#the full range of qualifiers (Brown tag QL) that appear before these four
#verbs.
import nltk
from nltk.corpus import brown
verbs=['adore', 'love', 'like', 'prefer']
#������������ 䳺�����,�� ��� ��� �� ������
text=nltk.corpus.brown.tagged_words(categories='news')
#���������� ����� text �� �����,�� �������� �� ������� brown �������
#news
a=[w for w in nltk.bigrams(text) if w[0][1].startswith
('QL') and w[1][1].startswith('V')]
#����� � ���������� �����,�� ���� ���������� ������ ��� � ����,��
#���������� �� ��� ������� ���� �������� �����
a
#�������� ��������� �� �����
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
#����� � ���������� �����,�� ���� ��������� �� ������� � ������ ������
#䳺�����
and w[1][1].startswith('V') and w[1][0] in verbs]
a
#��������� ��������� �� �����
text=nltk.corpus.brown.tagged_words(categories='romance')
#���������� ����� text �� �����,�� �������� �� ������� brown
#������� romance
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
#���� � ���������� �����,�� ���� ��������� �� ������� � ������
#������ 䳺�����
text=nltk.corpus.brown.tagged_words(categories='religion')
#���������� ����� text �� �����,��  �������� �� ������� brown
#������� religion
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
#����� � ���������� �����,�� ���� ��������� �� ������� � ������
#������ 䳺�����
text=nltk.corpus.brown.tagged_words(categories='news')
#���������� �� ���������� ���� �����,���� ����� ���� �������
#���� � ������� news
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0]=='operated']
#�����,���  �� �������� ����� � ����������,��� � ���� ������� ������
#�����,�� ��� ��� � ���� ������,� ���� adore,love,like,prefer

