#Anna Karbivska, Als-11
#7.9.6
#Write one or more tag patterns to handle coordinated noun phrases, e.g., July/
#NNP and/CC August/NNP, all/DT your/PRP$ managers/NNS and/CC supervisors/NNS,
#company/NN courts/NNS and/CC adjudicators/NNS.
import nltk
sentence = [ ("All", "DT"), ("your", "PRP$"), ("managers", "NNS"),("and","CC"),
             ("supervisors","NNS"), ("arrived", "VBD"), ("at","IN"),
             ("July", "NNP"), ("and", "CC"), ("August", "NNP")]#create sentence
grammar = "NP:{<DT>?<PRP$>?<NN.*>+<CC><NN.*>*}" #create ragular expression
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
result = cp.parse(sentence)#test chunk parser on my sentence
print result #print result
from nltk.corpus import conll2000 #import conll2000 corpus for making evaluation
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=('NP',))
print cp.evaluate(test_sents) #print evaluation
