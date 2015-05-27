
import nltk
grammar1 = nltk.parse_cfg("""
S -> NP_SG VP_1st_SG
S -> NP_SG VP_3rd_SG
NP_SG -> Pro
VP_1st_SG -> Cop_1st_SG_Adj
VP_3rd_SG -> Cop_3rd_SG_Adj
Cop_1st_SG ->'am'
Cop_3rd_SG ->'is'
PRO -> 'I' | 'She'
Adj -> 'happy'
Cop -> 'is | am '
""") 
print grammar1

# Result:grammar with 11 productions. Some rules required to correctly parsing of word sequences
