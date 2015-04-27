# імпортуємо необхідні для роботи програми модулі
import nltk 
import types
from nltk.corpus import senseval
# доступаємся до даних з корпусв
instances = senseval.instances('serve.pos')
features=[]
# перетворюємо instances до потрібного вигляду (списку кортежів кожен з яких складається зі словника та стрічки).
for inst in instances:
 zx=[]
 for i in inst.context:
 if (type(i) == types.TupleType):
 zx.append(i)
 elif (type(i) == types.StringType):
 zx.append(("None",i))
 a={"word": inst.word,"position": inst.position,}
 b=dict(zx)
 a.update(b)
 features.append((a,' '.join(inst.senses)))
# встановлюємо розмір даних для тестуваня (10%) 
size = int(len(features) * 0.1)
# ділимо всі дані на дві частини - для тренування і для тестування
train_set, test_set = features[size:], features[:size]
# тренуємо класифікатор
classifier1 = nltk.NaiveBayesClassifier.train(train_set)
# оцінюємо точність його роботи
print (nltk.classify.accuracy(classifier1, test_set))
