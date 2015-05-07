#by Ivanna Rurych, AL-12
#Chapter 5, Ex.25
#task: Obtain some tagged data for another language, and train and evaluate a variety of taggers on it. If the language is morphologically complex, or if there are an aphic clues (e.g., capitalization) to word classes, consider developing a regular expression tagger for it (ordered after the unigram tagger, and before the default tagger). How does the accuracy of your tagger(s) compare with the same taggers run on English data? Discuss any issues you encounter in applying these methods to the language.
import nltk
from nltk.corpus import brown
from nltk.corpus import mac_morpho
brown_tagged_sents = brown.tagged_sents(categories=['editorial','news']) #tagged 'editorial','news' categories of Brown Corpus
mac_morpho_tagged_sents = nltk.corpus.mac_morpho.sents()
train_s1 = brown_tagged_sents[:1000]
test_s1 = brown_tagged_sents[1000:3000]
train_s2 = mac_morpho.tagged_sents()[:1000]
test_s2 = mac_morpho.tagged_sents()[1000:3000] # Mac Morpho is tagged
unigram_English = nltk.UnigramTagger(train_s1) #use unigram tagger for English data
unigram_Brazilian_Portugese = nltk.UnigramTagger(train_s2)#use unigram tagger for Brazilian Portugese data
u1 = unigram_English.evaluate(test_s1)
u2 = unigram_Brazilian_Portugese.evaluate(test_s2)
bigram_English = nltk.BigramTagger(train_s1, backoff=unigram_English)#use Bigram tagger for English data
bigram_Brazilian_Portugese = nltk.BigramTagger(train_s2, backoff=unigram_Brazilian_Portugese)#use Bigram tagger for Brazilian Portugese data
b1 = bigram_English.evaluate(test_s1)
b2 = bigram_Brazilian_Portugese.evaluate(test_s2)
trigram_English = nltk.TrigramTagger(train_s1, backoff=bigram_English) #use Trigram tagger for English data
trigram_Brazilian_Portugese = nltk.TrigramTagger(train_s2, backoff=bigram_Brazilian_Portugese)#use Trigram tagger for Brazilian Portugese data
t1 = trigram_English.evaluate(test_s1)
t2 = trigram_Brazilian_Portugese.evaluate(test_s2)
print 'unigram_English', u1
print 'unigram_Brazilian_Portugese', u2
print 'bigram_English', b1
print 'bigram_Brazilian_Portugese', b2
print 'trigram_English', t1
print 'trigram_Brazilian_Portugese', t2
#I trained and evaluated unigram, bigram, and trigram taggers on the Brown (English language) and Mac_morpho (Brazilian Portugese) corpora. All these taggers work slightly better with Brazilian Portugese data.    
