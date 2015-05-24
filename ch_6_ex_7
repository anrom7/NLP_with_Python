#Chapter 6
#Exercise 7
#Author Sofiya Zaliska ALs-11
#The dialogue act classifier assigns labels to individual posts, without considering
#the context in which the post is found. However, dialogue acts are highly dependent
#on context, and some sequences of dialogue act are much more likely than
#others. For example, a ynQuestion dialogue act is much more likely to be answered
#by a yanswer than by a greeting. Make use of this fact to build a consecutive classifier
#for labeling dialogue acts. Be sure to consider what features might be useful.
#See the code for the consecutive classifier for part-of-speech tags in Example 6-5
#to get some ideas.
import nltk
posts = nltk.corpus.nps_chat.xml_posts()
history=[] # змінна для збереження типу попереднього повідомлення 
# функція для вилучення властивостей(ознак) з повідомлення
def dialogue_act_features(post,i,history):
    features = {}
        for word in nltk.word_tokenize(post):
            features['contains(%s)' % word.lower()] = True
            if i == 0:
                features["prev-class"] = ""
        else:
                features["prev-class"] = history[i-1] # тип попереднього повідомлення
            return features
        
featuresets=[]
for i, post in enumerate(posts): # обробляємо пронумерований список повідомлень
featuresets.append((dialogue_act_features(post.text, i, history), post.get('class')))
history.append(post.get('class')) # список типів всіх повідомлень
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)
0.644886363636
