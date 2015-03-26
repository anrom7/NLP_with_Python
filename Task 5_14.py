###Author Zemko Oksana

"""
Program creates a list of Brown Corpus tagset removing duplicates
"""

from nltk.corpus import brown
   tags=brown.tagged_words()
"""I created a list of tuples where I will gather tags in sorted list from"""

   just_tags=sorted(set([tag for (word, tag) in tags]))
"""sorted() makes a list of sorted in alphebet order tags,
set() makes a list of tags and they do not reduplicate,
expression in brackets pick up all tags in corpus"""
