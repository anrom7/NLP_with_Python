# Iryna Kupyak, PRLs-12, chapter 9, exercise 2
import nltk
nltk.data.show_cfg('grammars/book_grammars/kupyak_ex_2.fcfg') #виводимо на екран створену граматику
print '----------tree----------'
tokens = ' boy sings'.split()
from nltk import load_parser #import the load_parser function
cp = load_parser('grammars/book_grammars/kupyak_ex_2.fcfg', trace=2)
for tree in cp.nbest_parse(tokens):
	print tree
  
## Iryna Kupyak, PRLs-12, chapter 9, exercise 2
#% start S
# ###################
# Grammar Productions
# ###################
# S expansion productions
#S -> NP[NUM=?n] VP[NUM=?n]
# NP expansion productions
#NP[NUM=?n] -> N[NUM=?n, Count=Uncountable] 
#NP[NUM=?n] -> Det[NUM=?n, Count=Countable] N[NUM=?n] 
# VP expansion productions
#VP[TENSE=?t, NUM=?n] -> IV[TENSE=?t, NUM=?n]
#VP[TENSE=?t, NUM=?n] -> TV[TENSE=?t, NUM=?n] Adj
# ###################
# Lexical Productions
# ###################
#Det -> 'the' 
#N[NUM=sg] -> 'boy' | 'water' 
#N[NUM=pl] -> 'boys'  
#IV[TENSE=pres,  NUM=sg] -> 'sings'
#TV[TENSE=pres, NUM=sg] -> 'is' 
#IV[TENSE=pres,  NUM=pl] -> 'sing'
#Adj -> 'precious'
