#Gerych_Tetiana, PRLs-12, Chapter 5, Exercise 16

import nltk,re,pprint
from nltk.corpus import brown
fd=nltk.FreqDist(nltk.corpus.brown.words(categories='news'))
most_freq_words=fd.keys()[:30]
most_freq_words
print most_freq_words

cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
likely_tags=dict((word,cfd[word].max()) for word in most_freq_words)
baseline_tagger=nltk.UnigramTagger(model=likely_tags,backoff=nltk.DefaultTagger('NN'))
baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[30])
print baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[30])

baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))
print baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))

#without backoff
baseline_tagger=nltk.UnigramTagger(model=likely_tags)
baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[30])
print baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[30])

baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))
print baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))

#when a backoff tagger is omitted, the tagger performance for the various model sizes reduces
