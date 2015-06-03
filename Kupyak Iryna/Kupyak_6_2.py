# Iryna Kupyak, PRLs-12, Chapter 6 Ex. 2

import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])  # building a set of data
def gender_features(name):   # morphological characteristics of feature set
	features = {}
	features["firstletter"] = name[1].lower() # first letter of the name
	features['lastletter']=name[-1:].lower()  # last letter of the name
	return features



featuresets = [(gender_features(n), g) for (n,g) in names] # building data for the classifier
test_set=featuresets[500:]                                 # dividing data on test_set and train_set
dev_test_set = featuresets[500:1000]
train_set = featuresets[:6900]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)         # evaluating accuracy
print nltk.classify.accuracy(classifier, dev_test_set)
print classifier.show_most_informative_features(40)
