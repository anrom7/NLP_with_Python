
import nltk
from nltk.corpus import *

# “реную ён≥грамс“еггер на певних текстах ≥ перев≥р€ю на тестових реченн€х щоб досл≥дити €к≥сть роботи

brown_tagged_sents = brown.tagged_sents(categories='news')
sizeENG = int(len(brown_tagged_sents) * 0.9)
train_sentsENG = brown_tagged_sents[:sizeENG]
test_sentsENG = brown_tagged_sents[sizeENG:]
unigram_tagger = nltk.UnigramTagger(train_sentsENG)
print unigram_tagger.evaluate(test_sentsENG)
0.8110236220472441

Brazilian_tagged=mac_morpho.tagged_sents()[:1000]
size = int(len(Brazilian_tagged) * 0.9)
train_sentsBR = Brazilian_tagged[:size]
test_sents = Brazilian_tagged[size:]
unigram_tagger = nltk.UnigramTagger(train_sentsBR)
print unigram_tagger.evaluate(test_sents)
0.70929705215419503

