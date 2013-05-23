#Vezdenko Julia, Al-12, Task 2, Chapter 5
import nltk
from nltk.corpus import brown
fd = nltk.FreqDist(brown.words(categories = 'news'))
freq_words= fd.keys()# Searching the most frequent words
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
print 'access' in freq_words# We get True if the word is present in our text and False if not
print cfd ['access'].items()#  The frequency of the word as a noun or a verb
print 'blame' in freq_words
print cfd ['blame'].items()
print 'crush' in freq_words
print cfd ['crush'].items()
print 'demand' in freq_words
print cfd ['demand'].items()
print 'fight' in freq_words
print cfd ['fight'].items()
print 'grin' in freq_words
print cfd ['grin'].items()
print 'land' in freq_words
print cfd ['land'].items()
print 'match' in freq_words
print cfd ['match'].items()
print 'play' in freq_words
print cfd ['play'].items()
print 'support' in freq_words
print cfd ['support'].items()
# We pick a word that can be either a noun or a verb and can observe the frequency of this word.
# E.g. the word 'play' in the text is used 30 times as a verb and 11 times as a noun.
