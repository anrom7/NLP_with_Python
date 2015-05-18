### Chapter 7 task 7

import nltk
from nltk.corpus import conll2000
grammar="NP: {<VBG><NN.*><IN><DT|PRP$>?<NN>*}" # Задаю граматику
cp=nltk.RegexpParser(grammar)
test_sents = conll2000.chunked_sents('test.txt'[:100], chunk_types=['NP']) # Оцінka якoстi роботи чанкера на прикладі 100 тестових речень
print (cp.evaluate(test_sents))
sentence='Sharing books with her sister'
sentence=sentence.split()
tagged=nltk.pos_tag(sentence)
result=cp.parse(tagged)
print (result)
chunkscore = nltk.chunk.ChunkScore()
chunkscore.score(test_sents,result)
for chunk in chunkscore.incorrect(): # The chunks which were included in the guessed chunk structures, but not in the correct chunk structures, listed in input order.
	print (chunk)
for chunk in chunkscore.missed(): # The chunks which were included in the correct chunk structures, but not in the guessed chunk structures, listed in input order.
	print (chunk)
    
