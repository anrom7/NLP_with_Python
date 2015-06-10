
# Develope a simple chunker using regular expression
# chunker nltk.RegexpParser picking one of the chunk types
# in the CoNLL-2000 Chunking Corpus.

import nltk, re, pprint
from nltk.corpus import conll2000
# Picking corpus for further evaluations.
for sent in conll2000.chunked_sents("test.txt", chunk_types=["NP"])[:5]:
    print sent
grammar = "NP: {<DT>?<JJ>*<NN>}"
# Creating regular expression.
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"),
            ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")] 

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence) 
print result 
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
print cp.evaluate(test_sents)  
grammar = r"PP: {<[INNN].*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<IN><DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<NN>?<VB.*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP: {<JJ>?<IN>?<TO>?}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
# Accuracy 
# Precision
# Recall
# F-Measure
