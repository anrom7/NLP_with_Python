#julia vezdenko , al-12,chapter6 ,task6
import nltk
from nltk.corpus import senseval
instances = senseval.instances('serve.pos')
features=[]# Open corpus data
for inst in instances:
	context = [c if isinstance(c, tuple) else (c, "None") for c in inst.context]
        # Converting strings in "context" to (string, "None") tuples in order to create a dictionary
	f = dict(context)
	#Creating a dictionary
	f.update({"word": inst.word, "position": inst.position})
        # Updating features "word" and "position"
	features.append((f, ' '.join(inst.senses)))



size = int(len(features) * 0.1)# Set an amount of testing data (10%)
train_set, test_set = features[size:], features[:size]# Making two data sets (for training and testing)
classifier1 = nltk.NaiveBayesClassifier.train(train_set)# Training the classifier
print nltk.classify.accuracy(classifier1, test_set)#Evaluating the accuracy of the classifier
