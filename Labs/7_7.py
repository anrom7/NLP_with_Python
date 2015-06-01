#Turianska K., PrLs-11, Chapter_7_ex_7

# a

import nltk
grammar = r"NP: {<DT|JJ|NN>+}"
cp = nltk.RegexpParser(grammar)
chunkscore = nltk.chunk.ChunkScore()
forchunk_struct in nltk.corpus.treebank_chunk.chunked_sents()[:100]:
  test_sent = cp.parse(chunk_struct.flatten())
	chunkscore.score(chunk_struct, test_sent)
print chunkscore

# b
from random import shuffle
missed = chunkscore.missed()
shuffle(missed)
print missed[:10]

incorrect = chunkscore.incorrect()
shuffle(incorrect)
print incorrect[:10]

# c
grammar = r"NP: {<DT|JJ|NN>+}"
cp = nltk.RegexpParser(grammar)
print nltk.chunk.accuracy(cp, nltk.corpus.conll2000.chunked_sents()[:100])
