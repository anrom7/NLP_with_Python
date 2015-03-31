# fine
#Viktoriia Palianytsia
# Chapter 5, Task 24
# How serious is the sparse data problem? Investigate the performance of n-gram
#taggers as n increases from 1 to 6. Tabulate the accuracy score. Estimate the training
#data required for these taggers, assuming a vocabulary size of 105 and a tagset size
#of 102.
# 
#  sents=brown.sents() why?
# Sparse data problem occures when using N-gram Taggers. To identify the correct tag for word
#a tagger needs context. But when N is larger, the context is more specific. 
# When tagger "meets" the word he didn't see during training in such context, it would't tag it.
#Also when we will increase the amount of training data it would't solve the problem.
#That is why the sparse data problem is one of the most important in NLP.
#
#
import nltk
from nltk.corpus import brown
tagged_sents=brown.tagged_sents()
train_sents=tagged_sents[:1000] # dani dlia trenuvannja
diap=[1,2,3,4,5,6] # diapazon zna4enj
for i in diap:
	t=nltk.NgramTagger(n=i, train=train_sents)
	print 'N=',i, 'Evaluation:', t.evaluate (tagged_sents[1000:1200])
