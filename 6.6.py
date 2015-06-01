
import nltk
from nltk.corpus import brown
featureset=[]
context={}
for tagged_sent in brown.tagged_sents():
	for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
		 if t1.startswith('aa') and w1 == 'strong':
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
		 elif t1.startswith('aa') and w1 == 'powerful':
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
print featureset[100]
print featureset[125]
print featureset[350]
size = int(len(featureset) * 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
print classifier.classify({'sales':'NNS'})
print classifier.classify({'chip':'NN'})
