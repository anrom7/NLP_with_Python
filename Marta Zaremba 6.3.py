# Marta Zaremba PRLs-11
# Rozdil_6, Zadacha_3

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
	
