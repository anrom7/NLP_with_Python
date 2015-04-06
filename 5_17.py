# Chapter 5
# Exercise 17
# Author Svitlana Synytsia
'''
What is the upper limit of performance for a lookup tagger, assuming no limit
to the size of its table? (Hint: write a program to work out what percentage of tokens
of a word are assigned the most likely tag for that word, on average.)
'''
# lookup tager - пошуковий мовний аналізатор, він дає змогу знайти
# найчастотніші слова та теги до них
import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents()
# обробка послідовності речень і вивід на екран 100 найчастотніших
fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.keys()[:100]
# найчастотніший тег
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
# дані у відсотках
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
baseline_tagger.evaluate(brown_tagged_sents)
print baseline_tagger.evaluate(brown_tagged_sents)
