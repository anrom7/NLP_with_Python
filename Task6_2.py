#Chapter 6 task 2
#author Oksana Zemko

import nltk
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')])
"""
this part of program prepares a list of name examples
"""
def gender_features(name):
     features = {}
     features['first letter']= name[0]
     features['last letter']= name[-1]
     features['total amount']= len(name)
     for letter in 'abcdefghijklmnopqrstuvwxyz':
         features["count(%s)" % letter] = name.lower().count(letter)
         features["has(%s)" % letter] = (letter in name.lower())
     return features
"""
cycle presents first and last letter in names
"""
featuresets = [(gender_features(n), g) for (n,g) in names]
"""
create feature extractor to process the names data
"""
train_set, test_set, dev_test_set = featuresets[:6900], featuresets[500:], featuresets[500:1000]
"""
divide them into 3 groups
"""
classifier = nltk.NaiveBayesClassifier.train(dev_test_set)
classifier = nltk.NaiveBayesClassifier.train(test_set)
print(nltk.classify.accuracy(classifier,dev_test_set))
print(nltk.classify.accuracy(classifier,test_set))
"""
analyze classifier accuracy
"""

#точність послідовного класифікатора аналізу над помилками становить 66%
#точність послідовного класифікатора оцінки системи становить 80%
