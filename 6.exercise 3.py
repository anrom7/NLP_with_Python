#Fedorchak V,ALs-11
#chapter 6, task 3
import nltk
import types
from nltk.corpus import senseval #import senseval corpus
instances = senseval.instances('serve.pos') 
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


size = int(len(features) * 0.1) # determine the amount of data to check
train_set, test_set = features[size:], features[:size] # distribution of data for testing and training
classifier = nltk.NaiveBayesClassifier.train(train_set) # train classifier
print nltk.classify.accuracy(classifier, test_set)
