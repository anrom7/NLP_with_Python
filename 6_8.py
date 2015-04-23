###Chapter 6 task 8

import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)]

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
print (len(all_words))
word_features = list(all_words.keys())[:200]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print (nltk.classify.accuracy(classifier, test_set))
for word in list(all_words.keys())[:200]:
	if all_words[word]<all_words[list(all_words.keys())[250]]:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemmas:
					for l_names in list(all_words.keys()):
						if word not in word_features:
							word_features.append(word)
featuresets=[(document_features(d),c) for (d,c) in documents]
train_set,dev_set, test_set=featuresets[20:60],featuresets[60:], featuresets[:20]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print (nltk.classify.accuracy(classifier, dev_set))
print (nltk.classify.accuracy(classifier, test_set))

