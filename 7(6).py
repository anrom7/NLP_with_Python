#chaper 7, Ex. 6
#by Ivanna Rurych
import nltk
sentence = [("July", "NNP"), ("and", "CC"), ("August", "NNP"), ("all", "DT"), ("your", "PRP$"),
            ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS"), ("company", "NN"),
            ("courts", "NNS"), ("and", "CC"), ("adjudicators", "NNS")] 
grammar = "NP:{<DT|PRP\$|NN.*>+<CC><NN.*>+}" #regular expression rules
chunk_parser=nltk.RegexpParser(grammar) #chunk parser
print chunk_parser.parse(sentence) # print result
from nltk.corpus import conll2000 #Access the data of the CoNLL-2000 Chunking Corpus. 
test_sents=nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=['NP']) #We are interested in the NP chunks right now.  
print chunk_parser.evaluate(test_sents) #Evaluate chunker on the data for testing
