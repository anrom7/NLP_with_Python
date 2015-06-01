
import nltk
sentence=[("many","JJ"),("researchers","NNS"),("two","CD"),("weeks","NNS"),
          ("both","DT"),("new","JJ"),("positions","NNS")]
grammar = "NP: {<DT>*<JJ>*<CD>*<NN.*>+}" # Define a chunk grammar
bk=nltk.RegexpParser(grammar)# Using this grammar we create a chunk parser
result=bk.parse(sentence)#Test this chunk on our example
print result
from nltk.corpus import conll2000 # import conll2000 corpus
cp = nltk.RegexpParser(grammar)# using grammar create a chunk parser and test
                                #it on our sentence
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents) # print evaluation result
