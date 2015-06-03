import nltk, re, pprint
sentence = [("the","DT"), ("little","JJ"), ("black","JJ"),("dog", "NN"), ("barked","VBD"),("at","IN"),("the","DT"),("cat","NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar) # create chunk parser
result= cp.parse(sentence)
print result# print sentence
from nltk.corpus import conll2000 # import corpus conll2000
print conll2000.chunked_sents('train.txt',chunk_types = ['PP']) [49] #  Print the 50th sentence from the training set
test_sents = conll2000.chunked_sents('test.txt', chunk_types = ['PP'])#  Only read PP chunks and simple evaluation
print cp.evaluate(test_sents) # print ChunkParse score
grammar = r"PP:{<[INNN].*>+}"
cp = nltk.RegexpParser(grammar)# create chunk parser 
print cp.evaluate(test_sents)
grammar = r"PP:{<IN><DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar=r"PP:{<NN>?<VB.*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
grammar = r"PP:{<VB.*>?<NN.*>*<DT>*}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(test_sents)
# reselt we can see IOB tags accurancy indicates.
# However, since our tagger did not find any chunks, its precision,recall,f-measure are all zero.
