

import nltk
posts=nltk.corpus.nps_chat.xml_posts() 
history=[] # Змінна для збереження типу попереднього повідомлення (post’s dialogue act type) 
def dialogue_act_features(post,k,history): # Функція видалення повідомлення
    features={}
    for word in nltk.word_tokenize(posts):
        features['contains(%s)' %word.lower()]=True
        if k==0:
            features["prev-class"]=""
        else:
            features["prev-class"]=history[k-1]# Тип попереднього повідомлення
        return features


featuresets=[]
for i,posts in enumerate(posts): # Обчислення прорахованого списку повідомлення
	featuresets.append((dialogue_act_features(posts.text,i,history),posts.get('class')))
	history.append(posts.get('class'))
size=int(len(featuresets)*0.1)
train_set, test_set=featuresets[size:],featuresets[:size]# Створення двох наборів даних (тренування та тестування)
classifier=nltk.NaiveBayesClassifier.train(train_set) # тренування класифікатора
print nltk.classify.accuracy(classifier, test_set) #Оцінка точності класифікатора
