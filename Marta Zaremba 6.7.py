# Marta Zaremba, PRLs-11

import nltk
posts=nltk.corpus.nps_chat.xml_posts() #������� ����� � ��������
history=[] #���������� ������������ �����
def dialogue_act_features(post,i,history): #������� ��� ������ �������� �����
    features={}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' %word.lower()]=True
        if i==0:
            features["prev-class"]=""
        else:
            features["prev-class"]=history[i-1]
        return features

featuresets=[]
for i,post in enumerate(posts): #������� ��������������� ������ ����������
    featuresets.append((dialogue_act_features(post.text,i,history),post.get('class')))
    history.append(post.get('class'))
size = int(len(featuresets)*0.1)
train_set, test_set=featuresets[size:],featuresets[:size]
classifier=nltk.NaiveBayesClassifier.train(train_set) #������������
print nltk.classify.accuracy(classifier, test_set) #������ ����� �������������
