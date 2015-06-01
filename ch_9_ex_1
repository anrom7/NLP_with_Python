#Chapter 9
#Exercise 1
#Author Sofiya Zaliska ALs-11
#What constraints are required to correctly parse word sequences like I am happy
#and she is happy but not *you is happy or *they am happy? Implement two solutions
#for the present tense paradigm of the verb be in English, first taking Grammar
#(8) as your starting point, and then taking Grammar (20) as the starting point.
import nltk
grammar1 = nltk.parse_cfg("""  #The grammar is based on the model (8)
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
""")
print grammar1
# we want to avoid the original grammar being multiplied ( I is happy, They am happy)
