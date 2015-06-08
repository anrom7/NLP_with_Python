
import nltk
# access the data of the CoNLL-2000 Chunking Corpus. The corpus contains 270k words of 
# Wall Street Journal text, divided into “train” and “test” portions, annotated with
# part-of-speech tags and chunk tags in the IOB format.
from nltk.corpus import conll2000
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
print cp.evaluate(test_sents)
grammar = r"""
          PP:
          {<.*>+}
          }<NN|TO|PRP\$|JJ|CC|NN.|VB.>+{
          """ #{<.*>+} - Chunk everything. }<NN|TO|PRP$|JJ|CC|NN.|VB.>+{ - Chink sequences of NN,TO,PRP$,JJ,CC,NNS, NNP,VBZ
sentence= [("In", "IN"),("addition", "NN"),("to", "TO"),("his", "PRP$"),("previous", "JJ"),("real-estate", "NN"),
           ("investment", "NN"),("and", "CC"),("asset-management", "NN"),("duties", "NNS"),("Mr.", "NNP"),("Meador", "NNP"),
           ("takes", "VBZ"),("responsibility", "NN"),("for", "IN"),("development", "NN"),("and", "CC"),("property", "NN"),
           ("management", "NN")] # sentence that should be chunked.
chunk_parser=nltk.RegexpParser(grammar)# test chunk_parser on our sentence.The result is a tree,which we can print
print chunk_parser.parse(sentence)
chunk_parser = nltk.RegexpParser(grammar)# we are interested in the PP chunks right now.  
# so we can use the chunk_types argument to select them.
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
print chunk_parser.evaluate(test_sents)
