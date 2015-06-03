#Kupyak Iryna, PRLs-12, Chapter 6, Exercise 4
#Using the movie review document classifier discussed in this chapter, generate
#a list of the 30 features that the classifier finds to be most informative. Can you
#explain why these particular features are informative? Do you find any of them
#surprising?
import nltk
from nltk.corpus import movie_reviews
import random
documents= [(list(movie_reviews.words(fileid)),category)#Make a randomized list of pairs, words and category, for each fileid
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())# the most frequend word in owr text
word_features=all_words.keys() [:1500]# our 1500 words 
def document_features(document):#Function to create a document feature list.
    document_words= set(document)# our 1500 words, we have a feature which is the word and "true" or "false"
    features= {}
    for word in word_features:
         features['contains(%s)' % word] = (word in document_words)
    return features

featuresets= [(document_features(d), c) for (d,c) in documents]#here we actually call the function.
train_set, test_set = featuresets[:100], featuresets[:100]
classifier= nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(30)
# In this program, we can examine the classifier to determine which features it found most effective
#resulting in a system whose accuracy is about 0.5. I think this words are informative becouse they
# can have different meaning or positive or nagative features.

