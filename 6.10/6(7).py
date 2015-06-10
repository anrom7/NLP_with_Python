import nltk
posts = nltk.corpus.nps_chat.xml_posts() #The NPS Chat Corpus consists of over 10,000 posts.
                                         #Call xml_posts() to get a data structure representing the XML annotation for each post.
history=[] #This variable is used to save the type of the previous message.
def dialogue_act_features(post,i,history): #Define a simple feature extractor that checks what words the post contains
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
	if i == 0:
		features["prev-class"] = ""
	else:
		features["prev-class"] = history[i-1] #The type of the previous message
	return features

featuresets=[]
for i, post in enumerate(posts):
    featuresets.append((dialogue_act_features(post.text, i, history), post.get('class'))) #Construct the training and testing data by
	                                                                                      #applying the feature extractor to each post
    history.append(post.get('class')) #The list of types of all messages

	                               #Create a new classifier
size = int(len(featuresets) * 0.1) #Set the size of the data for training (10%)
train_set, test_set = featuresets[size:], featuresets[:size] #Divide all data in two parts - for training and testing 
classifier = nltk.NaiveBayesClassifier.train(train_set) #Train the classifier
print 'Accuracy %s' % nltk.classify.accuracy(classifier, test_set) #Evaluate the accuracy of the classifier

