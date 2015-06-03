# Hanchevska Iryna, Chapter 6, Exercise 5
# for this exercise I choose classification task, such as name gender detection
#and  built the classifier "NaiveBayesClassifier"
#also i have used the dev-test set for generating a list of the errors that the classifier makes when
#predicting name genders:
 
import nltk
from nltk.corpus import treebank

from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
def gender_features(word):
    return {'last_letter': word[-1]}

featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'Accuracy of NaiveBayesClassifier'
print nltk.classify.accuracy(classifier, test_set)


#select a development set, containing the
#corpus data for creating the model. This development set is then subdivided into the
#training set and the dev-test set.

train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'Accuracy of NaiveBayesClassifier with dev-test set'
print nltk.classify.accuracy(classifier, devtest_set)



#generating a list of the errors
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
    print 'correct=%-8s guess=%-8s name=%-30s' %(tag, guess, name)

# The second accuracy where the devtest_set is used is lower.
