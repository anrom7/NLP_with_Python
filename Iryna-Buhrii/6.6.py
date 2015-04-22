import nltk
from nltk.corpus import brown
featureset=[] # create set of features
context={}    # create different contexts
for tagged_sent in brown.tagged_sents(): # for words 'stong' and 'powerful' assigned appropriate features and contexts
	for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
		 if t1.startswith('JJ') and w1 == 'strong': 
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
		 elif t1.startswith('JJ') and w1 == 'powerful':
			 context[w2]=t2
			 featureset.append((context,w1))
			 context={}
print featureset[75] # results
print featureset[150]
print featureset[200]
size = int(len(featureset) * 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set) # prediction of use
print classifier.classify({'sales':'NNS'}) # combining with sales
print classifier.classify({'chip':'NN'})   # combining with chip
