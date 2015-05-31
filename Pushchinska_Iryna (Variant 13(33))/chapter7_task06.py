# Pushchinska_Iryna PRLs-11
# Chapter_7, Task_6

import nltk#importing data
posts = nltk.corpus.nps_chat.xml_posts()#The posts included 1)Hand privacy masked,2) Part-of-speech tagged; and
#3) Dialogue-act tagged.
history=[]#creating an empty list in wich we will write all the results
def dialogue_act_features(post,i,history):#function to get the type of message(define a feature extractor)
	features = {}#created an empty list
	for word in nltk.word_tokenize(post):#thi function is chacking whether the word is in the list and adding to the history
		features['contains(%s)' % word.lower()] = True
	if i == 0:
		features["prev-class"] = ""
	else:
		features["prev-class"] = history[i-1] 
	return features

featuresets = []
for i, post in enumerate(posts):#examine a numerated list
	featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
	history.append(post.get('class'))
#A feature extractor for document classification, whose features indicate whether or not individual words are present in a given document.
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)#To check how reliable the resulting classifier is, we compute its accuracy on the test set
#Conclusion: there are usually limits to the number of features that you should use with a given learning algorithm — if you provide too many features, then the algorithm will have a higher chance of relying on idiosyncrasies of your training data that don't generalize well to new examples. 
#This problem is known as overfitting, and can be especially problematic when working with small training sets. 
#For example, if we train a naive Bayes classifier using the feature extractor shown in Example 6.2, it will overfit relatively small training set, resulting in a system whose accuracy is about 1% lower than the accuracy of a classifier that only pays attention to the final letter of each name:
