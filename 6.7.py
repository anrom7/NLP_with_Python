
import nltk
posts=nltk.corpus.nps_chat.xml_posts() # Необхідні нам текстові файли з діалогами
history=[] # Змінна у якій зберігається попередній стан
def dialogue_act_features(post,i,history): # Створюю функцію для пошуку необхідних даних
	features={}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' %word.lower()]=True
		if i==0:
			features["prev-class"]=""
		else:
			features["prev-class"]=history[i-1]
		return features

	
featuresets=[]
for i,post in enumerate(posts): # Функція обробки пронумерованого списку повідомлень
	featuresets.append((dialogue_act_features(post.text,i,history),post.get('class')))
	history.append(post.get('class'))
size=int(len(featuresets)*0.1)
train_set, test_set=featuresets[size:],featuresets[:size]
classifier=nltk.NaiveBayesClassifier.train(train_set) # Створення класифікатора
print nltk.classify.accuracy(classifier, test_set) # Визначення якості роботи класифікатора

