
#Fedorchak V ALs-11

#Chapter 7, ex. 8

#Develop a chunker for one of the chunk types in the CoNLL Chunking Corpus
#using a regular expression–based chunk grammar RegexpChunk.





import nltk
from nltk import *
sentence=nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=('NP',))[99]
grammar=r"NP:{<[CDJNP].*>+}" #opusujy gramatuky, jaka bude vydiliaty fragmenty
#na osnovi reguliarnogo vyrazu jakyj opysue typovuj imennukovyj
#vuraz (poslidovnist tegiv CD J NP)

cp=nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print sentence
print result
result.draw()
