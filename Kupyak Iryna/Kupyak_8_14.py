# Iryna Kupyak, PRLs-12, chapter 8, exercise 14
#You can modify the grammar in the recursive descent parser demo by selecting
#Edit Grammar in the Edit menu. Change the first expansion production, namely
#NP -> Det N PP, to NP -> NP PP. Using the Step button, try to build a parse tree.
#What happens?

import nltk
from nltk import *

#creating grammar for the sentence "John goes home"
grammar1 = nltk.parse_cfg("""
S  -> NP VP
NP -> DET N PP
VP -> V NP
V -> "goes" 
NP -> "John"  
NP ->  "home" 
""")
sent_1 = "John goes home".split()
rd_parser_1 = nltk.RecursiveDescentParser(grammar1)
for tree_1 in rd_parser_1.nbest_parse(sent_1):
    print tree_1
tree_1.draw()

# Changing the first expansion production, namely
# NP -> Det N PP, to NP -> NP PP.

grammar1 = nltk.parse_cfg("""
S  -> NP VP
NP -> NP PP
VP -> V NP
V -> "goes" 
NP -> "John"  
NP ->  "home" 
""")
sent = "John goes home".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
    print tree
tree.draw()


# as a result we have an error:
#File "C:\Python26\lib\site-packages\nltk\tree.py", line 138, in __getitem__
#if isinstance(index, (int, slice)):
#RuntimeError: maximum recursion depth exceeded in __instancecheck__
