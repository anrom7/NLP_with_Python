# Anastasiya Ostapchuk
# PRLs-12
# Chapter 6, Exercise 7
# TODO: Using the WordNet lexicon, augment the movie review document classifier to use features that generalize thewords that appear in a document, making it more likely that they will match words found in the training data.

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents=[(list(movie_reviews.words(fileid)),category) 
	    for category in movie_reviews.categories()
	    	for fileid in movie_reviews.fileids(category)[:500]]
# creating the pairs of words in each document from the pos/neg category
random.shuffle(documents) 
all_review_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
print "The amount of words in the file with movie reviews"
print len(all_review_words)
word_features=all_review_words.keys()[:350]
# function that checks weather words we need are included in the document
def document_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['%contains' %word]=(word in document_words)
		return features

featuresets=[(document_features(d),c) for (d,c) in documents]
train_set, test_set=featuresets[100:], featuresets[:100]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print "The initial accuracy of the classifier"
print nltk.classify.accuracy(classifier, test_set) 
for word in all_review_words.keys()[:450]: 
	if all_review_words[word]<all_review_words[all_review_words.keys()[350]]:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemma_names:
					for l_names in all_review_words.keys()[:450]:
						if word not in word_features:
							word_features.append(word)


featuresets=[(document_features(d),c) for (d,c) in documents]
# creating training and testing data
train_set, test_set=featuresets[150:], featuresets[:150]
classifier=nltk.NaiveBayesClassifier.train(train_set) 
print "The final accuracy of the classifier"
print nltk.classify.accuracy(classifier, test_set)
