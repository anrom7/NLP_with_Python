# Anna Karbivska, Als-11
# 6.10.3
#The Senseval 2 Corpus contains data intended to train word-sense disambiguation
#classifiers. It contains data for four words: hard, interest, line, and serve.
#Choose one of these four words, and load the corresponding data:
#        >>> from nltk.corpus import senseval
#>>> instances = senseval.instances('hard.pos')
#>>> size = int(len(instances) * 0.1)
#>>> train_set, test_set = instances[size:], instances[:size]
#Using this dataset, build a classifier that predicts the correct sense tag for a given
#instance. See the corpus HOWTO at http://www.nltk.org/howto for information
#on using the instance objects returned by the Senseval 2 Corpus.

import nltk
import types
from nltk.corpus import senseval #import senseval corpus
instances = senseval.instances('serve.pos') # choose data  for word 'serve'
features=[]
for inst in instances:
	comtext=[]
	for i in inst.context:
		if type(i) == types.TupleType:
			comtext.append(i)
		elif type(i) == types.StringType:
			comtext.append(("None",i))
			word_position={"word": inst.word,"position": inst.position,}
			dictionary=dict(comtext)
			word_position.update(dictionary)
			features.append((word_position,' '.join(inst.senses)))

	
size = int(len(features) * 0.1) # choose data size for testing
train_set, test_set = features[size:], features[:size] # divide data for train and test
classifier = nltk.NaiveBayesClassifier.train(train_set) # train classifier
print nltk.classify.accuracy(classifier, test_set) #assess the accuracy of his work
	
