# Anastasiya Ostapchuk
# PRLs-12
# Chapter 7, Exercise 10
# TODO: Study the errors of bigram chunker.
# Try to work out why it doesn't get 100% accuracy

import nltk
import nltk.chunk
from nltk.corpus import conll2000
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
# looking for tags beginning with letters that are characteristic of noun phrase tags
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)

class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramChunker(train_data)
# changing the class name to BigramChunker, and modifying the line to construct a BigramTagger rather than a UnigramTagger

# using the parse method to chunk new sentences
    def parse(self, sentence): 
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
cp = nltk.RegexpParser(grammar)

print "Testing data accuracy"
print cp.evaluate(test_sents)

print "Training data accuracy"
print cp.evaluate(train_sents)

# Trying to add the different features to the feature extractor function,
# we see that we can further improve the performance of the NP chunker.
