#Fedorchak V,ALs-11
#chapter 6, task 7
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[]
def dialogue_act_features(post,i,history): # creating function of obtaining features
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

train_set, test_set = featuresets[1:9000], featuresets[9000:] # dividing test and train data
classifier = nltk.NaiveBayesClassifier.train(train_set)
print 'train set items =', len(train_set),' test set items =', len(test_set) 
print 'Accuraci', (nltk.classify.accuracy(classifier, test_set)*100.0),'%' 
# Dialog class identifier that uses not only the featuring words of diferrent posts but also the class of the previous post
