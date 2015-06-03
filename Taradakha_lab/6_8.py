#Kateryna Taradakha 6_8


import nltk, random
from nltk.corpus import movie_reviews, wordnet as wn
documents = [(list(movie_reviews.words(fileid)), category) 
                    for category in movie_reviews.categories() 
                    for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words() if len(w)>3)
word_features = all_words.keys()[:2000]
syn_word_features = [l_name for word in all_words.keys()[:500]
                            for synset in wn.synsets(word) if word in synset.lemma_names
                            for l_name in synset.lemma_names]
word_features+=list(set(syn_word_features))
def document_features(document):
    'extract features fom the document'
    document_words = set(document)
    features = {}
    for word in list(set(word_features)):
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(5)
                        
