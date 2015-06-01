# Marta Zaremba PRLs-11
# Rozdil_6, Zadacha_5

 import nltk# загрузила усі необхідні функції, корпуса, дані
 from nltk.corpus import names
 import random
 import math
 names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
 random.shuffle(names)# сортуємо імена
 def gender_features(word):#функція для визначення роду імені
	return {'last_letter': word[-1]}
print(gender_features('Peter-Nansy'))

featuresets = [(gender_features(n), g) for (n,g) in names]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

naiveBayesClassifier = nltk.NaiveBayesClassifier.train(train_set)
productivity=nltk.classify.accuracy(naiveBayesClassifier, test_set)# результат продуктичності класифікатора Баєра
def entropy(labels):# функція для визначення роду імен за допомогою ентропії
    freqdist = nltk.FreqDist(labels)
     probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
      return -sum([p * math.log(p,2) for p in probs])
    productivity=entropy(['male', 'female', 'male', 'male'])# результат продуктивності за допомогою ентропії
    # з цих результатів можна зробити висновки, що використовуючи ентропію ми маємо кращі результати аніж тоді, коли ми використовуємо методи пошуку, щоб знайти набір параметрів, які максимізують продуктивність classifier
