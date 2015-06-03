# Iryna Kupyak, PRLs-12, chapter 6, exercise 8
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents=[(list(movie_reviews.words(fileid)),category) 
	    for category in movie_reviews.categories()
	    	for fileid in movie_reviews.fileids(category)[:400]]

random.shuffle(documents) 
all_review_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_review_words)
word_features=all_review_words.keys()[:350]
def document_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['%contains' %word]=(word in document_words)
		return features

featuresets=[(document_features(d),c) for (d,c) in documents]
train_set, test_set=featuresets[40:], featuresets[:40]# Making two data sets (for training and testing)
classifier=nltk.NaiveBayesClassifier.train(train_set)# Training the classifier
print nltk.classify.accuracy(classifier, test_set) #Evaluating the basic accuracy of the classifier
for word in all_review_words.keys()[:450]: # Making hypernym frequencies bigger 
	if all_review_words[word]<all_review_words[all_review_words.keys()[350]]:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemma_names:
					for l_names in all_review_words.keys()[:350]:
						if word not in word_features:
							word_features.append(word)


featuresets=[(document_features(d),c) for (d,c) in documents]
train_set,dev_set, test_set=featuresets[40:80],featuresets[80:], featuresets[:40]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, dev_set) #Evaluating the accuracy of the classifier
print nltk.classify.accuracy(classifier, test_set) 

