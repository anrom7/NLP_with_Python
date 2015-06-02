# Anastasiya Ostapchuk
# PRLs-12
# Chapter 7, Exercise 2
# TODO: Write a tag pattern to match noun phrases containing plural head nouns.
# Try to generalize it.

import nltk
sentence=[("Harry", "NNP"), ("writes", "VBD"), ("the", "DT"), ("main", "JJ"), ("patterns", "NNS"), ("in", "IN"), ("the", "DT"), ("workbook","NN")]
grammar = "NP: {<DT>?<JJ>*<NN.*>+}" # creating the chunk grammar
cp = nltk.RegexpParser(grammar) # creating chunk parser with the use of grammar 
result = cp.parse(sentence) # testing chunk parser on the sentence
print "Results of the chunking the sentences with plural nouns:"
print result
