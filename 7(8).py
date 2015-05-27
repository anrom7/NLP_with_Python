#chapter 7, Ex 8
#by Ivanna Rurych, PRLs-12
import nltk
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus. 
tcp = nltk.RegexpParser("") #the trivial chunk parser 
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
print tcp.evaluate(test_sents)
grammar = r"""
PP:
{<.*>+}                       
}<NN|TO|PRP\$|JJ|CC|NN.|VB.>+{
"""  #{<.*>+} - Chunk everything. }<NN|TO|PRP$|JJ|CC|NN.|VB.>+{ - Chink sequences of NN,TO,PRP$,JJ,CC,NNS, NNP,VBZ
sentence= [("July", "NNP"), ("and", "CC"), ("August", "NNP"), ("all", "DT"), ("your", "PRP$"),
            ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"), ("company", "NN"),
            ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")]  #Sentence that should be chunked.
chunk_parser=nltk.RegexpParser(grammar) #Create a chunk parser
print chunk_parser.parse(sentence) #print result
chunk_parser = nltk.RegexpParser(grammar)#Once more create a chunk parser
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])#We are interested in the PP chunks right now.  
print chunk_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
