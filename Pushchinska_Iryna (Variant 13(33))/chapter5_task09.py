# Pushchinska_Iryna PRLs-11
# Chapter_5, Task_9

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(['I', 'like', 'this', 'wristwatch'])# print tagged sentence

# Some words are not assigned a tag,
# becouse these words are not stored inside the tagger.

