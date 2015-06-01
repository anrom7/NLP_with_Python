# Визначаємо рід імені

import nltk ##import all necessary functions, corpus, data
from nltk.corpus import names
import random
import math
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
def gender_features(word): ## функція визначення роду імені
    return {'last_letter': word[-1]}
    print(gender_features('Peter-Nansy'))

    
featuresets = [(gender_features(n), g) for (n,g) in names]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

naiveBayesClassifier = nltk.NaiveBayesClassifier.train(train_set)
productivity=nltk.classify.accuracy(naiveBayesClassifier, test_set)
##результат з BayesClassifier
def entropy(labels):## функція визначення роду імені з використанням ентропії
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])
productivity=entropy(['singular', 'plural', 'singular', 'plural'])
print productivity
## результат продуктивності ентропії
## З використанням ентропії ми покращуємо результати, оскільки відбувається використання пошукових засобів для знаходження наборів параметрів, що збільшують виконання класифікатора

