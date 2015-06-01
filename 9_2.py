#Chapter 9 task 2
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
% start S
# ###################
# Grammar Productions
# ###################
# S expansion productions
S -> NP[NUM=?n] VP[NUM=?n]
# NP expansion productions
NP[NUM=?n] -> N[NUM=?n] 
NP[NUM=pl] -> N[NUM=pl] 
NP[NUM=?n] ->DetN[NUM=?n]
# VP expansion productions
VP[TENSE=?t, NUM=?n] -> IV[TENSE=?t, NUM=?n]
VP[TENSE=?t, NUM=?n] ->Cop[TENSE=?t, NUM=?n] Adj
# ###################
# Lexical Productions
# ###################
Det ->'the' | 'The'
N[NUM=sg] -> 'boy' | 'water' | 'Water' 
N[NUM=pl] -> 'boys'
IV[TENSE=pres,  NUM=sg] -> 'sings'
IV[TENSE=pres,  NUM=pl] -> 'sing'
Cop[TENSE=pres, NUM=sg]-> 'is'
Adj-> 'precious'
