# vezdenko julia al-12 task4 chapter9
import nltk
from nltk import load_parser #import the load_parser function
parser = load_parser('grammars/book_grammars/feat0.fcfg')
#VP[TENSE=?t, NUM=?n] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n] # expansion productions
#VP[TENSE=?t, NUM=?n] -> V[SUBCAT=trans, TENSE=?t, NUM=?n] NP
#VP[TENSE=?t, NUM=?n] -> V[SUBCAT=clause, TENSE=?t, NUM=?n] SBar
#V[SUBCAT=intrans, TENSE=pres, NUM=sg] -> 'disappears' | 'walks' # lexical Productions
#V[SUBCAT=trans, TENSE=pres, NUM=sg] -> 'sees' | 'likes'
#V[SUBCAT=clause, TENSE=pres, NUM=sg] -> 'says' | 'claims'
#V[SUBCAT=intrans, TENSE=pres, NUM=pl] -> 'disappear' | 'walk'
#V[SUBCAT=trans, TENSE=pres, NUM=pl] -> 'see' | 'like'
#V[SUBCAT=clause, TENSE=pres, NUM=pl] -> 'say' | 'claim'
#V[SUBCAT=intrans, TENSE=past] -> 'disappeared' | 'walked'
#V[SUBCAT=trans, TENSE=past] -> 'saw' | 'liked'
#V[SUBCAT=clause, TENSE=past] -> 'said' | 'claimed'
tokens = 'girl walks'.split() 
parser = load_parser('grammars/book_grammars/feat0.fcfg')
for tree in parser.nbest_parse(tokens):    # data- tree output 
         print tree
