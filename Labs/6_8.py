Turianska K., PrLs-11, Chapter_6_ex_8
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
docs=[(list(movie_reviews.words(fileid)),category)
           for categ in movie_reviews.categories()
           for fid in movie_reviews.fileeids(categ)]
random.shuffle(docs) #constracting a list of documents,labelded with the appropriate categories
allWords=nltk.FrequDist(w.lower() for in movie_rewiews.words())
print len(allWords)
wordFeatures=allWords.keys()[:2000]
allWords=nltk.FrequDist(w.lower() for w in movie_reviews.words())
wordFeatures=allWords.keys()[:2000]

def documentsFeatures(document):
    documentWords=set(documents)
    features={}
    for word in word_features:
        features['contains(%s)'% word]= (word in documentWords)
        return features  #checking if word is located in document
    features=[documentFeatures(d),c)for (d,c)in documents]
    train_set,test_set=featuresets[100:],featuresets[:100]
    classifier=nltk.NaivebayersClassifier.train(train_set)
    print nltk.classify.accuracy(classifier,test_set)

    for words in all-words.keys()[:3000]:
        if allWords[words]<allWords[allWords.key()[2000]]:
            for synset in wn .synset.hypernyms():
                for 1_names in hypernyms():
                    if 1_names in allWords.keys()[:2000]:
                        if word not in word_features:
                            wordFeatures.append(word)
                            print len(wordFeatures)
                            featuresets=[(documentFeatures(d),c) for (d,c)in documents]
                            train_set,test_set=featuresset[100:],featureset[:100]
                            classfier=nltk.NaiveBayesClassifier.train(train_set)
                            print.nltk.classify.accurancy (classifier,test_set) #computing its accuracy on the test set 
