# Anna Karbivska, Als-11
# 5.10.16
# Compare tagger performance with and without backoff tagger.

>>> import nltk,re,pprint
>>> from nltk.corpus import brown
>>> frdist=nltk.FreqDist(nltk.corpus.brown.words(categories='news'))
>>> mfreqword=frdist.keys()[:50]
>>> mfreqword
>>> print mfreqword
>>> cfrdist=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
>>> tag_util=dict((word,cfrdist[word].max()) for word in mfreqword)
>>> baseline_tagger=nltk.UnigramTagger(model=tag_util,backoff=nltk.DefaultTagger('NN'))
>>> baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[50])
>>> print baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[50])
>>> baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))
# Using backoff tagger. Result is 53.4%.
>>> print baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))
>>> baseline_tagger=nltk.UnigramTagger(model=tag_util)
>>> baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[50])
>>> print baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[50])
>>> baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))
>>> print baseline_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='news'))
# Omitting backoff tagger. Result is 40%, which is quite worse.
# Conclusion: Omitting the backoff tagger makes the tagger less performant.
