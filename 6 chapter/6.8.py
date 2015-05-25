# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# Chapter 6 (exercise 8)
# Word features can be very useful for performing document classification, since the words that appear in a document give a strong indication about what its semantic content is. However, many words occur very infrequently, and some of the most informative words in a document may never have occurred in our training data. One solution is to make use of a lexicon, which describes how different words relate to one another. Using WordNet lexicon, augment the movie review document classifier presented in this chapter to use features that generalize the words that appear in a document, making it more likely that they will match words found in the training data.

import nltk, random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
# Make a randomized list of pairs, words and category, for each fileid
documents=[(list(movie_reviews.words(fileid)),category)
	    for category in movie_reviews.categories()
	    	for fileid in movie_reviews.fileids(category)[:100]]
random.shuffle(documents)
all_review_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_review_words)
word_features=all_review_words.keys()[:250]
# Function to create a document feature list.  For each of our 200 words, we have  the word and "true" or "false"
def document_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['%contains' %word]=(word in document_words)
		return features
featuresets=[(document_features(d),c) for (d,c) in documents]
# Create our train set and test sets, run the classifier
train_set, test_set=featuresets[20:], featuresets[:20]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
for word in all_review_words.keys()[:300]:
	if all_review_words[word]<all_review_words[all_review_words.keys()[200]]:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemma_names:
					for l_names in all_review_words.keys()[:200]:
						if word not in word_features:
							word_features.append(word)
featuresets=[(document_features(d),c) for (d,c) in documents]
train_set,dev_set, test_set=featuresets[20:60],featuresets[60:], featuresets[:20]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, dev_set)
print nltk.classify.accuracy(classifier, test_set) 

