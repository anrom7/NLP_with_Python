# Hanchevska Iryna, Chapter 5, Exercise 18
import nltk
from nltk.corpus import brown
brown_adventure_tagged = brown.tagged_words(categories='adventure', simplify_tags=True)
data = nltk.ConditionalFreqDist((word.lower(), tag)
                                for (word, tag) in brown_adventure_tagged)
for word in data.conditions():
    if len(data[word]) == 1:
        tags = data[word].keys()
        print word, ' '.join(tags)
        
#Розглядаю у корпусі Brown слова, яким відповідає один тег,
#тобто які є однозначними.

for word in data.conditions():
    if len(data[word]) > 2:
        tags = data[word].keys()
        print word, ' '.join(tags)

#Розглядаю у корпусі Brown слова, яким відповідає два і більше тегів,
#тобто які є багатозначними.
#Результат показав, що кількість багатозначних слів є значно більшою,
#ніж кількість однозначних.
#Після проведення обчислень(вручну) визначаю, що кількість неоднозначних слів становить 53, а однозначних - 7523.
#В процентному відношенні, кількість неоднозначних слів - 0,07%, кількість однозначних - 99,3.


