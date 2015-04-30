# Anastasiya Ostapchuk
# PRLs-12
# Chapter 6, Exercise 5
# TODO: Classify some text using three classifiers: a decision tree, a naive Bayes classifier, and a Maximum Entropy classifier.
#       Compare the results.

import nltk 
from nltk.corpus import names
import random
import math
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names) # mixing

# function for determining the gender of name
def gender_features(word): 
    return {'last_letter': word[-1]}

print "Testing the function:"
print gender_features('Bobby')

featuresets = [(gender_features(n), g) for (n,g) in names]
# creating the set of touples to connect endings with gender
train_set, test_set = featuresets[1000:], featuresets[:1000]
# training and testing data were created

nbc = nltk.NaiveBayesClassifier.train(train_set)
# testing the Naive Bayes Classifier on training data
productivity=nltk.classify.accuracy(nbc, test_set)
# calculating the Naive Bayes Classifier accuracy
print "The accuracy of the Naive Bayes Classifier:"
print productivity

# creating the function for determining the gender of name using entropy
def entropy(labels):
    fd = nltk.FreqDist(labels)
    probs = [fd.freq(i) for i in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])

productivity2=entropy(['male', 'female', 'male', 'male'])
print "The accuracy of the Entropy Classifier:"
print productivity2
