# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# Chapter 6 (exercise 4)
# Using the movie review document classifier discussed in this chapter, generate a list of the 30 features that the classifier finds to be most informative. Can you explain why these particular features are informative? Do you find any of them surprising?

import nltk, random
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) # Створюю список оглядів фільмів
	     for category in movie_reviews.categories()
	     for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
# Створення функції для пошуку необхідних даних
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
	        features['contains(%s)' % word] = (word in document_words)
    return features
# Поділ даних на частини
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
#Створення класифікатора і визначення найінформативніших слів
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(30)