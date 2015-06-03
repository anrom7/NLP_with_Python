# Iryna Kupyak, PRLs-12, Chapter 7 Ex.7


import nltk
from nltk.corpus import conll2000 # import corpus conll2000
grammar="NP: {<DT|IN|PRP|NN>?<VBG><DT>?<NN>*}" #creating a rule for the grammar
cp=nltk.RegexpParser(grammar) # create a Chunk parser using a grammar
test_sents = conll2000.chunked_sents('test.txt'[:100], chunk_types=['NP']) # Evaluate the work of a chunker on the basis of 100 senyences from corpus Conll 2000                                                                            #the basis of 100 sentences of corpus Conll2000 
print cp.evaluate(test_sents)
sentence='The little kitten came in into the room'
sentence=sentence.split()
tagged=nltk.pos_tag(sentence)
result=cp.parse(tagged)
print result
tagged=nltk.pos_tag(sentence)
result=cp.parse(tagged)
print result
chunkscore = nltk.chunk.ChunkScore()
chunkscore.score(test_sents,result)
for chunk in chunkscore.incorrect(): #The chunks which were included in the guessed chunk structures, but not in the correct chunk structures, listed in input order. 
	print chunk
	
for chunk in chunkscore.missed(): #The chunks which were included in the correct chunk structures, but not in the guessed chunk structures, listed in input order.
	print chunk

