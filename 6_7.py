# Chapter 6
# Exercise 7
# Author Svitlana Synytsia
'''
The dialogue act classifier assigns labels to individual posts, without considering
the context in which the post is found. However, dialogue acts are highly dependent
on context, and some sequences of dialogue act are much more likely than
others. For example, a ynQuestion dialogue act is much more likely to be answered
by a yanswer than by a greeting. Make use of this fact to build a consecutive classifier
for labeling dialogue acts. Be sure to consider what features might be useful.
See the code for the consecutive classifier for part-of-speech tags in Example 6-5
to get some ideas.
'''
import nltk
posts=nltk.corpus.nps_chat.xml_posts() 
history=[] # A variable to save the type of previous message (post’s dialogue act type) 
def dialogue_act_features(post,i,history): #A function to delete message features
        features={}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' %word.lower()]=True
		if i==0:
			features["prev-class"]=""
		else:
			features["prev-class"]=history[i-1]# Type of the previous message
		return features


featuresets=[]
for i,post in enumerate(posts): # Working out the enumerated message list
	featuresets.append((dialogue_act_features(post.text,i,history),post.get('class')))
	history.append(post.get('class'))
size=int(len(featuresets)*0.1) # the establishment of ize
train_set, test_set=featuresets[size:],featuresets[:size]# Making two data sets (for training and testing)
classifier=nltk.NaiveBayesClassifier.train(train_set) # Training the classifier
print nltk.classify.accuracy(classifier, test_set) #Evaluating the accuracy of the classifier
