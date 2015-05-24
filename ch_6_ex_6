#Chapter 6
#Exercise 6
#Author Sofiya Zaliska ALs-11
#The synonyms strong and powerful pattern differently (try combining them with
#chip and sales). What features are relevant in this distinction? Build a classifier that
#predicts when each word should be used.
import nltk
from nltk.corpus import brown
featureset=[]
context={}
for tagged_sent in brown.tagged_sents():
for (w1,t1), (w2,t2) in nltk.bigrams(tagged_sent):
if t1.startswith('JJ') and w1 == 'strong':
context[w2]=t2
featureset.append((a,w1))
context={}
elif t1.startswith('JJ') and w1 == 'powerful':
context[w2]=t2
featureset.append((a,w1))
context={}
# дивимось що отримали
featureset[5]
({'New': 'JJ-TL'}, 'powerful')
len(featureset)
253
# в корпусі всього 253 випадків вживання цих прикметників.
size = int(len(featureset) * 0.1)
train_set, test_set = featureset[size:], featureset[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)
0.59999999999999998
classifier.classify({'fight':'NN'})
'strong'
classifier.classify({'fight':'v'})
'strong'
classifier.classify({'fight':'JJ'})
'strong'
classifier.classify({'fight':'VB'})
'strong'
classifier.classify({'chip':'NN'})
'strong'
