import nltk
from random import shuffle
grammar = r'NP:  {<DT|JJ|NN>+}'
cp = nltk.RegexpParser(grammar)
chunkscore = nltk.chunk.ChunkScore()
for file in nltk.corpus.treebank_chunk.files()[:5]:
	for chunk_struct in nltk.corpus.treebank_chunk.chunked_sents(file):
		test_sent = cp.parse(chunk_struct.flatten())
		chunkscore.score(chunk_struct, test_sent)

correct = chunkcore.correct()
shuffle(correct)
print incorrect[:30]
