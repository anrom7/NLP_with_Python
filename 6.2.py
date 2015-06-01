import nltk
from nltk.corpus import names
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')]) 	# Змінна у якій міститьсь інформація про імена і статі

def gender_features(name): # Створюємо функцію яка буде видобувати лексичні особливості імен
        features = {}
        features["lastletter"] = name[-1].lower()
        features["suffix1"] = name[-2:].lower()
        features["suffix2"] = name[-3:].lower()
        features["suffix3"] = name[-4:].lower()
        return features
# Розподіляємо корпус імен на 3 частини згідно умови завдання
featuresets = [(gender_features(n), g) for (n,g) in names]
test_set = featuresets[500:]
dev_test_set = featuresets[500:1000]
train_set = featuresets[:6900]
# Створюємо класифікатор NaiveBayes
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, dev_test_set)
print nltk.classify.accuracy(classifier, test_set)
print classifier.show_most_informative_features(20)

