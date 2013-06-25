#presented by Volkov Mark PRLc 11
# Chapter 9, Ex.1

#The grammar is based on the model (8)
S ->N_SG VP_1st_SG 
S ->N_SG  VP_3rd_SG  
NP_SG ->PRO
VP_1st_SG -> Cop_ 1st_SGAdj
VP_3rd_SG -> Cop_ 3rd_SGAdj
Cop_ 1st_SG->'am'
Cop_ 3rd_SG->'is'
PRO-> 'I' | 'She'
Adj -> 'happy'

#The grammar is based on the model (20)
S -> NP[AGR=?n] VP[AGR=?n]
NP[AGR=?n] -> N[AGR=?n]
VP[TENSE=?t, AGR=?n] ->Cop[TENSE=?t, AGR=?n] Adj
Cop[TENSE=pres, AGR=[NUM=sg, PER=1]] -> 'am'
Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] ->'is'
N[AGR=[NUM=sg, PER=1]] -> 'I'
N[AGR=[NUM=sg, PER=3]] -> 'She'
Adj ->'happy'
