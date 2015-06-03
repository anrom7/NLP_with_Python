
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
documents=[(list(movie_reviews.words(fileid)),category) 
	    for category in movie_reviews.categories()
	    	for fileid in movie_reviews.fileids(category)[:500]]

random.shuffle(documents) 
all_review_words=nltk.FreqDist(word.lower() for word in movie_reviews.words())
print len(all_review_words)
word_features=all_review_words.keys()[:450]
def pos_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['%contains' %word]=(word in document_words)
		return features

featuresets=[(pos_features(d),c) for (d,c) in documents]
train_set, test_set=featuresets[40:], featuresets[:40]# 2 набори даних (випробування та тестування)
classifier=nltk.NaiveBayesClassifier.train(train_set)# Випробовування класифікатора
print nltk.classify.accuracy(classifier, test_set) #Оцінення основної точності класифікатора
for word in all_review_words.keys()[:550]: # збільшуємо частоту гіперніму 
	if all_review_words[word]<all_review_words[all_review_words.keys()[450]]:
		for synset in wn.synsets(word):
			for hypernyms in synset.hypernyms():
				for l_names in hypernyms.lemma_names:
					for l_names in all_review_words.keys()[:450]:
						if word not in word_features:
							word_features.append(word)


featuresets=[(pos_features(d),c) for (d,c) in documents]
train_set,dev_set, test_set=featuresets[40:80],featuresets[80:], featuresets[:40]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, dev_set) #Оцінення точності класифікатора
print nltk.classify.accuracy(classifier, test_set) 

