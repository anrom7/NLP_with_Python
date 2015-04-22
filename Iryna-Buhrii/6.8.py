import nltk
import random
from nltk.corpus import movie_reviews 
                                     
from nltk.corpus import wordnet as wn 
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words()) 
word_features = all_words.keys()[:300] 
                                       
def document_features(document):                                
    document_words = set(document)
	                             
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[150:], featuresets[:150] #Divide all data in two parts - for training and testing 
classifier = nltk.NaiveBayesClassifier.train(train_set) #Train the classifier
print nltk.classify.accuracy(classifier, test_set) #Evaluate the accuracy of the classifier
for word in all_words.keys()[:400]: #If the word didn't get to the list of the most frequent words, but 
                                    #its hypernyms are in this list, 
                                    #Then this word should be added to the list of the most frequent words
    if all_words[word]< all_words[all_words.keys()[300]]:
        for synset in wn.synsets(word):
            for hypernyms in synset.hypernyms():
                for l_names in hypernyms.lemma_names:
                    if l_names in all_words.keys()[:300]:
                        if word not in word_features:
                            word_features.append(word) #Add word to the list of most frequent words
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[150:], featuresets[:150] #Once more divide all data in two parts - 
                                                           #for training and testing (now with added words)
classifier = nltk.NaiveBayesClassifier.train(train_set) #Once more train the classifier
print len(word_features) 
#As a result 353 words have been added to the list of the most frequent words. 
#The training of the classifier was carried out several times, but its accuracy didn't increase.
#0.746666666667      0.7     0.66             0.746666666667
#353                 353     353              353
#0.746666666667      0.72    0.693333333333   0.8



