#
# Author Oksana Zemko
#

"""
This program is created to count a full range of qualifiers in Brown corpus that precede such words as adore, love, like, prefer
"""

import nltk
from nltk.corpus import brown
tagged_w=brown.tagged_words()
"""
tagging words in corpus
"""
bigrams_brown=nltk.bigrams(tagged_w)
"""
using bigrams to have access to 2 tuples of corpus to get pattern(...'QL'),('adore/love/like/prefer')
"""
ql_brown=[]
"""
created empty list where words-qualifiers will be added
"""
for i,j in bigrams_brown:
	    if i[1] == 'QL' and (j[0] == 'adore' or j[0] == 'love' or j[0] == 'like' or j[0] == 'prefer'):
	         ql_brown.append(i[0])
"""
cicle that looks for required pattern
when finding appropriate one adding word-qualifier to the list
"""
result=sorted(set(ql_brown))
"""
removing duplicates of words-qualifiers and sorting them in alphabet order
"""
