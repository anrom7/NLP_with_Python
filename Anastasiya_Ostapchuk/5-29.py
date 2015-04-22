# Anastasiya Ostapchuk
# PRLs-12
# Chapter 5, Exercise 29
# TODO: Write a program to find some examples of bigram tagger failures.

import nltk
from nltk.corpus import brown

# example
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
word_tag_pairs = nltk.bigrams(brown_news_tagged)
print "The tags list:"
print list(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'N'))

# other examples
# creating tagger
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
# creating training and testing data
train_sents = brown_tagged_sents[:2000]
test_sents = brown_tagged_sents[2000:]

bigram_tagger = nltk.BigramTagger(train_sents)
print "Accuratly tagged sentences:"
print bigram_tagger.tag(brown_sents[1500])

unseen_sent = brown_sents[4540]
print "Failures in tagged sentences:"
print bigram_tagger.tag(unseen_sent)

print "The accuracy of the bigram tagger:"
print bigram_tagger.evaluate(test_sents)



