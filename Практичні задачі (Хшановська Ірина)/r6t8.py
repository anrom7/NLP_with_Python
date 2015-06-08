# TODO
# Comments?
# How does your program work?



import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category)
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)[:100]]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
print len(all_words)
word_features = all_words.keys()[:200]
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

featuresets = [(document_features(d),c) for (d,c) in documents]
train_set, test_set = featuresets[90:], featuresets[:30]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
for word in all_words.keys()[:300]:
	if all_words[word] < all_words[all_words.keys()[200]]:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemma_names:
					if l_names in all_words.keys()[:200]:
						if word not in word_features:
						    word_features.append(word)

						    
print len(word_features)
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[90:], featuresets[:30]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
