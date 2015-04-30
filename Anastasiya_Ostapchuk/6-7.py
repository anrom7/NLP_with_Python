# Anastasiya Ostapchuk
# PRLs-12
# Chapter 6, Exercise 7
# TODO: Build a consecutive classifier for labeling dialogue acts.

import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[]
# creating function for obtaining features
def dialogue_act_features(post,i,history): 
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
		if i == 0:
			features["prev-class"] = ""
		else:
			features["prev-class"] = history[i-1] # obtaining class of the previous post from list "history"
	return features

featuresets=[] 
for i, post in enumerate(posts): 
	featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
	history.append(post.get('class'))
# creating training and testing data	
train_set, test_set = featuresets[:9000], featuresets[9000:] 
classifier = nltk.NaiveBayesClassifier.train(train_set)
# the classifier was created
print 'Items in training set =', len(train_set)
print 'Items in testing set =', len(test_set) 
print 'Accuracy of the classifier:', (nltk.classify.accuracy(classifier, test_set)*100.0),'%'
