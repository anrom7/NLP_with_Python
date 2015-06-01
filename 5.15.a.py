import nltk
from nltk.corpus import brown
sing=[]
pl=[]
for (w,t) in brown.tagged_words(categories='news'): # Відбір слів які мають тег іменника в однині.
	if t=='NN':
		sing.append(w)

fdistsing = nltk.FreqDist(sing) # Створення частотного списку вищевказаних слів

for (w,t) in brown.tagged_words(categories='news'): # Відбір слів які мають тег іменника в множині і додавання у список без останньої літери
	if t=='NNS':
		pl.append(w[:-1])

fdistpl = nltk.FreqDist(pl) # Створення частотного списку вищевказаних слів

for i in fdistpl.keys():	# Порівняння частоти входження в списки іменників. Якщо частота входженнь більша у множині ніж у однині то відбуваєтсья вивід на екран цього слова.
	if fdistpl[i]>fdistsing[i]:
		print i
