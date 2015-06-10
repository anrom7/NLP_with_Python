import nltk
from nltk.corpus import movie_reviews
documents=[(list(movie_reviews.words(fileid)),category)
	   for category in movie_reviews.categories()
	   for fileid in movie_reviews.fileids(category)]
import random
random.shuffle(documents)
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=all_words.keys()[:100]
def document_features(document):
	document_words=set(document)
	features={}
	for word in word_features:
		features['contains(%s)' %word]=(word in document_words)
	return features
    
featuresets=[(document_features(d),c) for (d,c) in documents]
train_set, test_set=featuresets[10:],featuresets[:10]
classifier=nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier,test_set)
classifier.show_most_informative_features(30)

# the program gathered all documents from movie_reviews
# then chose random words and assigned them features
# then made the accuracy of classifier