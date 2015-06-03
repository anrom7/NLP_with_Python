# Iryna Kupyak, PRLs-12, chapter 9, exercise 3

import nltk
fs1=nltk.FeatStruct(TENSE='past', NUM='sg')
fs2=nltk.FeatStruct(TENSE='past', NUM='sg', GND='fem', ARG=fs1)
print fs1
print fs2
print fs1.subsumes (fs2) #checking if fs1 subsumes fs2
print fs2.subsumes (fs1) #checking if fs2 subsumes fs1

# with this function we hold two feature structures fs1 and fs2
#just in case fs1 subsumes fs2.

def subs (fs1, fs2):
	if fs1.subsumes (fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes (fs1):
		print fs2.unify(fs1)
	else: print "None"
	
	
