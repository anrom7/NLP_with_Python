# Fedorchak V  ALs-11
import nltk
grammar8 = nltk.parse_cfg("""
S -> NP_3rd_SG VP_3rd_SG
S -> NP_PL VP_PL
S -> N V
VP_3rd_SG -> V_3rd_SG JJ
VP_PL -> V_PL JJ
V -> V JJ
N_3rd_SG -> 'she' | 'he' | 'it'
N_PL -> 'you' | 'we' | 'they'
N -> 'I'
V_3rd_SG -> 'is'
V_PL -> 'are'
V -> 'am'
JJ -> 'happy'
""")
print grammar8
#grammar20 
#S -> NP[AGR=[NUM=sg, PER=3]] VP[AGR=[NUM=sg, PER=3]]
#S -> NP[AGR=[NUM=pl]] VP[AGR=[NUM=pl]]
#S -> NP[AGR=?n] VP[AGR=?n]
#NP[AGR=[NUM=sg, PER=3]] -> N[AGR=[NUM=sg, PER=3]]
#P[AGR=[NUM=pl]] -> N[AGR=[NUM=pl]]
#NP[AGR=?n] -> N[AGR=?n]
#VP[TENSE=?t, AGR=[NUM=sg, PER=3]] -> Cop[TENSE=?t, AGR=[NUM=sg, PER=3]] Adj
#P[TENSE=?t, AGR=[NUM=pl] -> Cop[TENSE=?t, AGR=[NUM=pl]] Adj
#VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj
#Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
#Cop[TENSE=pres, AGR=[NUM=pl]] -> 'are'
#Cop[TENSE=pres, AGR=?n] -> 'am'
#N[AGR=[NUM=sg, PER=3]] -> 'she' | 'he' | 'it'
#N[AGR=[NUM=pl]] -> 'you' | 'we' | 'they'
#N[AGR=?n] -> 'I'
#Adj -> 'happy'

