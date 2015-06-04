
# Уляна Щомак ПРЛс-12 



import nltk
from random import shuffle
grammar = "NP: {<DT>?<JJ>*<NN>}"  # grammar rules
cp = nltk.RegexpParser(grammar)   # using a grammar we creat a chunk parser
chunkscore = nltk.chunk.ChunkScore()
for file in nltk.corpus.treebank_chunk.files()[:10]:
       for chunk_struct in nltk.corpus.treebank_chunk.chunked_sents(file):
              test_sent = cp.parse(chunk_struct.flatten())
chunkscore.score(chunk_struct, test_sent)

correct = chunkscore.correct()
shuffle(correct)
print correct[:13]
