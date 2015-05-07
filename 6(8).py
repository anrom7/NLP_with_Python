#be Ivanna Rurych, AL-12
#Chapter 6, Ex.8
import nltk
import random
from nltk.corpus import movie_reviews #Access to the data of the Movie Reviews Corpus
from nltk.corpus import wordnet as wn #Access to the data of the WordNet, a semantically oriented dictionary of English 
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words()) #identify the words of a text that are most frequent
word_features = all_words.keys()[:300] #Limit the number of features that the classifier needs to 
                                       #process (300 most frequent words in the overall corpus)
def document_features(document): #Define a feature extractor for documents, to help the classifier to identify which aspects of the data it should pay attention to
    document_words = set(document) #Check whether a word occurs in a set 
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[150:], featuresets[:150] #Divide all data in two parts - for training and testing 
classifier = nltk.NaiveBayesClassifier.train(train_set) #Train the classifier
print nltk.classify.accuracy(classifier, test_set) #Evaluate the accuracy of the classifier
for word in all_words.keys()[:450]: #If the word didn't get to the list of the most frequent words, but 
                                    #its hypernyms are in this list, 
                                    #Then this word should be added to the list of the most frequent words
    if all_words[word]< all_words[all_words.keys()[300]]:
        for synset in wn.synsets(word):
            for hypernyms in synset.hypernyms():
                for lemma_names in hypernyms.lemma_names:
                    if lemma_names in all_words.keys()[:300]:
                        if word not in word_features:
                            word_features.append(word) #Add word to the list of most frequent words
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[200:], featuresets[:200] #Once more divide all data in two parts - 
                                                           #for training and testing (now with added words)
classifier = nltk.NaiveBayesClassifier.train(train_set) #Once more train the classifier
print len(word_features) #Show the number of words that are added to the list
print nltk.classify.accuracy(classifier, test_set) #Once more evaluate the accuracy of the classifier
#as a result we would have 3 lines:the accuracy of the classifier; the number of words that are added to the list; updated accuracy of the classifier
#As a result 353 words have been added to the list of the most frequent words. 
#The training of the classifier was carried out several times, but its accuracy didn't increase.
#0.746666666667      0.7     0.66             0.746666666667
#353                 353     353              353
#0.746666666667      0.72    0.693333333333   0.8



