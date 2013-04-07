##Khrystyna Maschakhevich, AL-13, Chapter 6, Task 7. The task was to create constructive classifier for marking a dialog
##It was recommended to examine code of example 5-6.
## To get to the argument history, which contains the list of tags, which were predicted,
##we need to expand the function of characteristics extractor. Each tag in history corresponds to the word in the sentance.
## We need to point out that histiry will contain only tags of already marked words.
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[] ## variable for saving the previous type of message

def dialogue_act_features(post,i,history): ## function to get the type of message
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
	if i == 0:
		features["prev-class"] = ""
	else:
		features["prev-class"] = history[i-1] ## the type of previous message
	return features

featuresets = []
for i, post in enumerate(posts): ## examine a numerated list
	featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
	history.append(post.get('class'))## list of all messages

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
accuracy=nltk.classify.accuracy(classifier, test_set)##accuracy
