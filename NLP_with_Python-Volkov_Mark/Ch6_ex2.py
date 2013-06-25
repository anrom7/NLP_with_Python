# error
#presented by Volkov Mark PRLc 11
# Chapter 6, Ex.2
import nltk
def gender_features(name): # features extractor
  features = {}
	features['firstletter'] = name[0].lower()
	features['one_lastletter'] = name[-1:].lower()
	features['two_lastletter'] = name[-2:].lower()
	features['three_lastletter'] = name[-3:].lower()
	if len(name)>3:
		features['four_lastletter'] = name[-4:].lower()
		return features
	from nltk.corpus import names
	import random # 
	names = ([(name, 'male') for name in 
		names.words('male.txt')] + [(name, 'female') for name in 
			names.words('female.txt')]) #set of date
	random.shuffle(name) # creating set of names
	dev_names, train_names, test_names = names[:500], names[1000:], names[500:1000] #datasets
	train_set = [(gender_features(n) for (n, g) in train_names)]
	dev_set = [gender_features(n) for (n, g) in dev_names]
	test_set = [gender_features(n) for (n, g) in test_names]
	classifier = nltk.naiveBayesClassifier.train(train_set)
	errors = []
	for(name, tag)in dev_test_names:
		guess = classifier.classify(gender_features(names))
	if guess != tag:
		# with dev_test set we generate a list of the errors 
        # that the classifier makes when precidings name genders  
		errors.append ( (tag, guess, name) )

def gender_predicting(name):
	classifier.classify(gender_features(name))
	print 'Name:', name, ' Gender:', classifier .classfy(gender.features(name))
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, dev_test_set) #evaluating accuracy
	print nltk.classify.accuracy(classifier, test_set)



"""
 I have created classifier , with suchset of features as first letter, 
 last letter, two last letters and three last letters. 
 This module generate a number of errors.
"""

