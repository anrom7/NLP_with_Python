#Chapter 7
#Exercise 3
#Author Sofiya Zaliska ALs-11
#Pick one of the three chunk types in the CoNLL-2000 Chunking Corpus. Inspect the data and try to observe any patterns in the POS tag sequences that make up
#this kind of chunk. Develop a simple chunker using the regular expression chunker nltk.RegexpParser. Discuss any tag sequences that are difficult to chunk reliably.
import nltk, re, pprint
sentence = [("the","DT"), ("tall","JJ"), ("angry","JJ"), ("man", "NN"), ("yelled","VBD"),("at","IN"),("the","DT"),("dog","NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}" #create rule for grammar
cp = nltk.RegexpParser(grammar) # Chunk parser
result= cp.parse(sentence)
print (result) # Printing the result
from nltk.corpus import conll2000
print (conll2000.chunked_sents('train.txt',chunk_types = ['PP']) [49]) # Printing the 50th sentence from the training set
test_sents = conll2000.chunked_sents('test.txt', chunk_types = ['PP'])
print (cp.evaluate(test_sents)) # Printing ChunkParse score
grammar = r"PP:{<[INNN].*>+}"
cp = nltk.RegexpParser(grammar) #Chunk parser
print (cp.evaluate(test_sents))
grammar = r"PP:{<IN><DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
print (cp.evaluate(test_sents))
grammar=r"PP:{<NN>?<VB.*>+}"
cp = nltk.RegexpParser(grammar)
print (cp.evaluate(test_sents))
grammar = r"PP:{<VB.*>?<NN.*>*<DT>*}"
cp = nltk.RegexpParser(grammar)
print (cp.evaluate(test_sents))
