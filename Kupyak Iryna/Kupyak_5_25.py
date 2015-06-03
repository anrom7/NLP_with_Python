# Iryna Kupyak, PRLs-12, chapter 5, exercise 25
import nltk
from nltk.corpus import brown
from nltk.corpus import mac_morpho
brown_tagged_sents = brown.tagged_sents(categories='editorial')
mac_morpho_tagged_sents = nltk.corpus.mac_morpho.sents()
train_sents1 = brown_tagged_sents[:1000]
test_sents1 = brown_tagged_sents[1000:3000]
train_sents2 = mac_morpho.tagged_sents()[:1000]
test_sents2 = mac_morpho.tagged_sents()[1000:3000]
unigram_English = nltk.UnigramTagger(train_sents1)
unigram_Brazilian_Portugese = nltk.UnigramTagger(train_sents2)
u1 = unigram_English.evaluate(test_sents1)
u2 = unigram_Brazilian_Portugese.evaluate(test_sents2)
bigram_English = nltk.BigramTagger(train_sents1, backoff=unigram_English)
bigram_Brazilian_Portugese = nltk.BigramTagger(train_sents2, backoff=unigram_Brazilian_Portugese)
b1 = bigram_English.evaluate(test_sents1)
b2 = bigram_Brazilian_Portugese.evaluate(test_sents2)
trigram_English = nltk.TrigramTagger(train_sents1, backoff=bigram_English)
trigram_Brazilian_Portugese = nltk.TrigramTagger(train_sents2, backoff=bigram_Brazilian_Portugese)
t1 = trigram_English.evaluate(test_sents1)
t2 = trigram_Brazilian_Portugese.evaluate(test_sents2)
print 'unigram_English', u1
print 'unigram_Brazilian_Portugese', u2
print 'bigram_English', b1
print 'bigram_Brazilian_Portugese', b2
print 'trigram_English', t1
print 'trigram_Brazilian_Portugese', t2
#I trained and evaluated unigram, bigram, and trigram taggers on the Brown (English language) and Mac_morpho (Brazilian Portugese) corpora. All these taggers work slightly better with English data.    
