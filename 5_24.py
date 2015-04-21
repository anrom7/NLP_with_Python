import nltk
from nltk.corpus import brown
tagged=brown.tagged_sents(categories='learned', simplify_tags=True)
train_data=tagged
for w in range (1,6):
	ngram=nltk.NgramTagger (w, tagged)
	print ('ngram, n=', w, ngram.evaluate(nltk.corpus.brown.tagged ()))
