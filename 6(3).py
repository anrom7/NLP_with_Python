#by Ivanna Ryruch, AL-12
#Chapter 6, Ex.3
import nltk
import types
from nltk.corpus import senseval # The Senseval 2 Corpus contains data intended to train word-sense disambiguation  classifiers
senseval.fileids() #The Senseval 2 corpus contains data for 4 words: hard, interest, line, and serve.
instances = senseval.instances('hard.pos') #I chose one of these words: "hard"
features=[] #Transform instances to a needed look: list of tuples, each of them contains a dictionary and string. 
            #The variable 'features' will be this list. 
for inst in instances:
	list1=[] #Create an empty list 
	for i in inst.context: #Access to the elements of Senseval instance
		if type(i) == types.TupleType: #If the type of the element is tuple then
			list1.append(i) #add this element to the empty list 'list1'
		elif type(i) == types.StringType: #If the type of the element is tuple then
			list1.append(("None",i)) #add the word "None" and this element to 'list1'
	a={"word": inst.word,"position": inst.position,} #create a dictionary (and assign it to a), to which we 
	                                                 #add words and their positions
	b=dict(list1) #create a dictionary 'b' from a 'list1'. 
	a.update(b) #add all items from the dictionary 'b' to the dictionary 'a'
	features.append((a,' '.join(inst.senses))) #add the dictionary 'a' to the dictionary 'features'. 
	                                           #Dictionary 'features' has a look of list of tuples. 
				                   #Tuples consist of dictionary 'a' + string, which note the word's sense.
size = int(len(features) * 0.1) #Set the size of the data for training (10%)
train_set, test_set = features[size:], features[:size] #divide all data in two parts - for training and testing 
classifier = nltk.NaiveBayesClassifier.train(train_set) #Train the classifier
print 'Accuracy: %4.2f' % nltk.classify.accuracy(classifier, test_set) #evaluate the accuracy of the classifier
