#Turianska K, PrLs-11, Chapter_6_ex_7
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[] #variable for saving the previous type of message

def dialogue_act_features(post,i,history): #function to get the type of message
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
	if i == 0:
		features["prev-class"] = ""
	else:
		features["prev-class"] = history[i-1] #type of previous message
	return features

featuresets = []
for i, post in enumerate(posts): #examining a numerated list
	featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
	history.append(post.get('class'))#list of all messages

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
accuracy=nltk.classify.accuracy(classifier, test_set)#accuracy
