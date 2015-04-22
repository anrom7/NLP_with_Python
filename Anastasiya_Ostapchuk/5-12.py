# Anastasiya Ostapchuk
# PRLs-12
# Chapter 5, Exercise 12
# TODO: Create a bigram tagger with no backoff tagger. Try it on different data. What will happen?

import nltk
from nltk.corpus import brown
data=brown.tagged_sents(categories='mystery')
train_sents = data[:1000]
test_sents = data[1000:]
# training and testing data were created
bigram_tagger = nltk.BigramTagger(train_sents)
# a bigram tagger was created
b_sents=brown.sents()
# this is a variable, which contains sentences from corpus Brown
bigram_tagger.tag(b_sents[2000])
unseen_sent = b_sents[3500] # new data
print "Some part of the sentences:"
print  b_sents
print "Sentences that had been tagged:"
bigram_tagger.tag(unseen_sent)
print bigram_tagger.tag(unseen_sent)
print "The accuracy of the bigram tagger tried on training data:"
bigram_tagger.evaluate(train_sents)
print bigram_tagger.evaluate(train_sents)
print "The accuracy of the bigram tagger tried on testing data:"
bigram_tagger.evaluate(test_sents)
print bigram_tagger.evaluate(test_sents)

