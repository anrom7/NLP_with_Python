##Khrystyna Maschakhevich, AL-13, Chapter 6, Task 5.The task was to select one of the classification, I have chosen gender detection,
##using the same training and test data to build classificators and to compare the productivity of that classifiers
import nltk ##import all necessary functions, corpus, data
from nltk.corpus import names
import random
import math
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)## shuffle names
def gender_features(word): ## function for determining the gender of name
    return {'last_letter': word[-1]}
    print(gender_features('Peter-Nansy'))

    
featuresets = [(gender_features(n), g) for (n,g) in names]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

naiveBayesClassifier = nltk.NaiveBayesClassifier.train(train_set)
productivity=nltk.classify.accuracy(naiveBayesClassifier, test_set)
##result from productivity from BayesClassifier
def entropy(labels):## function for determining the gender of names using entropy
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])
productivity=entropy(['male', 'female', 'male', 'male'])## result of productivity from entropy
## taking to consideration results, i want to make the conclusion. My research showed that
##using entropy we can have better results, as is uses search techniques to find a set of parameters that will maximize the performance of the ckassifier.
