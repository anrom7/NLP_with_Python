
import nltk #importing data
import types
from nltk.corpus import senseval #The Senseval 2 corpus is a word sense disambiguation corpus. 
#Each item in the corpus corresponds to a single ambiguous word.
#For each of these words, the corpus contains a list of instances, corresponding to occurences of that word. 
#Each instance provides the word; a list of word senses that apply to the word occurrence; and the word's context.
instances = senseval.instances('serve.pos')#change instances to needed look
features=[]#empty list of couples
for instance in instances:
	emptylist=[]
	for i in instance.context:#one of the methods to access to the elements of Senseval instance
		if type(i) == types.TupleType:#The type of tuples (e.g. (1, 2, 3, 'Spam')); alias of the built-in tuple.
			emptylist.append(i)#adding to emptylist
		elif type(i) == types.StringType:#The type of character strings (e.g. 'Spam'); alias of the built-in str.
			emptylist.append(("None",i))#adding to emptylist
	a={"word": instance.word,"position": instance.position,}
	b=dict(emptylist)
	a.update(b)
	features.append((a,' '.join(instance.senses)))
size = int(len(features) * 0.1)#setting a size for a testing data
train_set, test_set = features[size:], features[:size]
classifier1 = nltk.NaiveBayesClassifier.train(train_set)#NaiveBayesClassifier is using as a baseline, using boolean word feature extraction
print nltk.classify.accuracy(classifier1, test_set)#eccurancy of a work
