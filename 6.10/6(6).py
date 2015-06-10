# Valerii Androshchuk APL(s)- 13.
# Chapter 6, Task 6.
# Build a classifier that predicts when the words strong and powerful shell be used.

import nltk
from nltk.corpus import brown
featureset = []
context={}
for tagged_sent in brown.tagged_sents():
	for (w1,t1),(w2,t2) in nltk.bigrams(tagged_sent):
		if t1.startswith('JJ') and w1 =='strong': 
			context[w2]=t2
			featureset.append((context,w1))
			context={}
			# Selecting the word "strong".
		if t1.startswith ('JJ') and w1 =='powerful':
			 context [w2] =t2
			 featureset.append((context,w1))
			 context={}
			 #Selecting word "powerful" for the further work.

			 
print featureset[1]
# Illustration with strong N_1
print featureset[4]
# Illustration with strong N_2
print featureset[16]
# Illustration with powerful N_1
print featureset[25]
# Illustration with powerful N_2
size = int(len(featureset) * 0.01) 
train_set, test_set = featureset[size:], featureset[:size] 
classifier = nltk.NaiveBayesClassifier.train(train_set)
# I built the classifier that predicts when these words shell be used.
# I was not able to combine them with "chip" and "sales"
# So I've decided to make two illustrations for each of them, but in different situation.


