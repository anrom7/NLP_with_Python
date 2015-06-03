# Taradakha K 6_5


import random, nltk
from nltk.corpus import names


def gender_features(word):
    features = {}
    features['suffix1'] = word[-1:]
    features['suffix2'] = word[-2:]
    return features
    
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, dev_test_set, test_set  = featuresets[:500], featuresets[500:1000], featuresets[1000:]
Naive_classifier = nltk.NaiveBayesClassifier.train(train_set)
Decision_classifier = nltk.DecisionTreeClassifier.train(train_set)
Maximum_Entropy_classifier=nltk.MaxentClassifier.train(train_set)
print 'NaiveBayesClassifier'
print str(round(100* nltk.classify.accuracy(Naive_classifier, test_set))) + '% Accuracy'

print 'DecisionTreeClassifier'
print str(round(100* nltk.classify.accuracy(Decision_classifier, test_set))) + '% Accuracy'

print 'Maximum_Entropy_classifier'
print str(round(100* nltk.classify.accuracy(Maximum_Entropy_classifier, test_set))) + '% Accuracy'
