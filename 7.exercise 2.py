#Fedorchak V, ALs-11

import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"),
          ("both","DT"),("new","JJ"),("positions","NNS")]
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" #Chunk grammar
bk=nltk.RegexpParser(grammar) #Creating chunk parser
result=bk.parse(sentence) #Examing the chunk on the example
print result
from nltk.corpus import conll2000
cp = nltk.RegexpParser(grammar) #Creating a chunk parser and testing it on the example
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)# Printing results
