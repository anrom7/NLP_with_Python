# Chapter 5
# Exercise 24
# Author Svitlana Synytsia
'''
How serious is the sparse data problem? Investigate the performance of n-gram
taggers as n increases from 1 to 6. Tabulate the accuracy score. Estimate the training
data required for these taggers, assuming a vocabulary size of 10 5 and a tagset size
of 10 2 .
'''
# Sparse data problem occures when using N-gram Taggers. To identify the correct tag for word
#a tagger needs context. But when N is larger, the context is more specific. 
# When tagger "meets" the word he didn't see during training in such context, it would't tag it.
#Also when we will increase the amount of training data it would't solve the problem.
#That is why the sparse data problem is one of the most important in NLP.
#
import nltk
from nltk.corpus import brown
brown_news_tagged=brown.tagged_sents(categories='news', simplify_tags=True)
test=brown.sents(categories='news')
# побудова циклу з н-грам тегів від 1 до 6
for n in range (6):
	ngram=nltk.NgramTagger(n, brown_news_tagged)
	ngram.tag(test[3])
	print ngram.evaluate(brown_news_tagged)# функція evaluate оцінює результати
