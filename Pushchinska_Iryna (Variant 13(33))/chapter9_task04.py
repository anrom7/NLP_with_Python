# Pushchinska_Iryna PRLs-11
# Chapter_9, Task_4

import nltk
from nltk import load_parser
cp=load_parser('grammars/book_grammars/feat0.fcfg') # import the load_parser function
#VP[TENSE=?t, NUM=?n] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n] 
#VP[TENSE=?t, NUM=?n] -> V[SUBCAT=trans, TENSE=?t, NUM=?n] NP
#VP[TENSE=?t, NUM=?n] -> V[SUBCAT=clause, TENSE=?t, NUM=?n] SBar
#V[SUBCAT=intrans, TENSE=pres, NUM=sg] -> 'disappears' | 'walks'
#V[SUBCAT=trans, TENSE=pres, NUM=sg] -> 'sees' | 'likes'
#V[SUBCAT=clause, TENSE=pres, NUM=sg] -> 'says' | 'claims'
#V[SUBCAT=intrans, TENSE=pres, NUM=pl] -> 'disappear' | 'walk'
#V[SUBCAT=trans, TENSE=pres, NUM=pl] -> 'see' | 'like'
#V[SUBCAT=clause, TENSE=pres, NUM=pl] -> 'say' | 'claim'
#V[SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked'
#V[SUBCAT=trans, TENSE=past] -> 'saw' | 'liked'
#V[SUBCAT=clause, TENSE=past] -> 'said' | 'claimed'
tokens='children walk'.split() 
for tree in cp.nbest_parse(tokens): # tree output 
         print tree
