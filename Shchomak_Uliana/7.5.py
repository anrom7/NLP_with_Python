
# ����� ����� ����-12 

import nltk
from nltk.corpus import conll2000
grammar="NP: {<DT|IN|PRP|NN>?<VBG><IN>?<DT>?<NN.*>+}" # ���� ��������� �������
cp=nltk.RegexpParser(grammar) # ������� ������
sentence='My brother found me wishing upon the falling star' # ����� �������
sentence=sentence.split()
tagged=nltk.pos_tag(sentence)
result=cp.parse(tagged)
result=cp.parse(tagged)
print result
#(S
#  My/PRP$
#  brother/NN
#  found/VBD
#  (NP me/PRP wishing/VBG upon/IN the/DT falling/NN star/NN))

