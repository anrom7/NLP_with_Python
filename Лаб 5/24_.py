

import nltk
from nltk.corpus import brown
tagged_sents=brown.tagged_sents()
train_sents=tagged_sents # data for training
for i in range (1,7): # range= from 1 to 6
	n_grams = nltk.NgramTagger (i, nltk.corpus.brown.tagged_sents()[:1000])
	print  'N_gram, N=',i, n_grams.evaluate(nltk.corpus.brown.tagged_sents()[1000:1200])
