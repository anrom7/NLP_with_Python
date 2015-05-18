#Chapter_6_Ex_7
#Viktoriia_Palianytsia_ALs-11
import nltk
posts = nltk.corpus.nps_chat.xml_posts()#dani z korpusu NPS_Chat
history = []
def dialogue_act_features(post,i,history):#funkcija dlya poshuku danyh
	features = {} 
	for word in nltk.word_tokenize(post):
		features['contains(%s)'% word.lower()] = True#vyznachennya sliv yaki mistut' povidomlennja
		if i ==0:
			features["prev-class"]=""
			
		else:
			features["prev-class"]= history[i-1]
		return features

	
featuresets = []
for i, post in enumerate(posts):# funkciya dlya obrobky pronumerovanogo spysku povidomlenj
	featuresets.append((dialogue_act_features(post.text,i,history), post.get('class')))
	history.append(post.get('class'))#spysok vsih typiv povidomlenj

	
size = int(len(featuresets)*0.1)# vkazuju rozmir danyh 
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)# stvorjuju klasyfikator
print nltk.classify.accuracy(classifier, test_set)# ocinka tochnosti textu

