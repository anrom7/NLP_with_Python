# bad
# TODO
# Comments?
#

import nltk
from nltk import*
d1={}.fromkeys(['help', 'room', 'red']) # словник1
d2={}.fromkeys(['phone', 'ask', 'clean', 'member']) # словник2
d1['help']='V'
d1['room']='N'
d1['red']='A'
d2['phone']='N'
d2['ask']='V'
d2['clean']='A'
d2['member']='N'
d1.update(d2) # оновлення словника
d1
print d1
# dodae dani d2 do slovnuka d1
# dodae dani z slovnyka d2 z klychamu, kotrux nemae v d1
