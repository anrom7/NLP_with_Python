#IMarta Zaremba, PRLs-11,  Chapter 9, task 16
import nltk
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
# Grammar Productions
# S expansion productions
grammar=("""
S-> NP VP[TENSE=?t]
# NP expansion productions
NP ->DetN
# VP expansion productions
VP[TENSE=?t] -> IV[TENSE=?t] Det N P N
VP[TENSE=?t] -> IV[TENSE=?t] N P Det N 
# LexicalProductions
Det -> 'The'| 'the'
N -> ' farmer ' | ' cart ' | 'sand' 
IV[TENSE=past] -> 'loaded' | 'filled'
P-> ' into ' | 'with '
""")
