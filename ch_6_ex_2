#Chapter 6
#Exercise 2
#Author Sofiya Zaliska ALs-11
#Using any of the three classifiers described in this chapter, and any features you
#can think of, build the best name gender classifier you can. Begin by splitting the
#Names Corpus into three subsets: 500 words for the test set, 500 words for the
#dev-test set, and the remaining 6,900 words for the training set. Then, starting with
#the example name gender classifier, make incremental improvements. Use the devtest
#set to check your progress. Once you are satisfied with your classifier, check
#its final performance on the test set. How does the performance on the test set
#compare to the performance on the dev-test set? Is this what you’d expect?
import nltk
from nltk.corpus import names #importing corpus of names
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
#точність послідовного класифікатора аналізу над помилками складає 74%
#точність послідовного класифікатора оцінки сиcтеми складає 76%
