# TODO
#In Table 3-1, we saw a table involving frequency counts for the verbs adore,
#love,like, and prefer, and preceding qualifiers such as really. Investigate
#the full range of qualifiers (Brown tag QL) that appear before these four
#verbs.
import nltk
from nltk.corpus import brown
verbs=['adore', 'love', 'like', 'prefer']
#перераховуємо дієслова,які дані нам за умовою
text=nltk.corpus.brown.tagged_words(categories='news')
#Присвоюємо змінній text усі слова,які належать до корпусу brown категорії
#news
a=[w for w in nltk.bigrams(text) if w[0][1].startswith
('QL') and w[1][1].startswith('V')]
#змінній а присвоюємо умову,за якою виводиться біграма слів і тегів,які
#визначають до якої частини мови належить слово
a
#виводимо результат на екран
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
#змінній а присвоюємо умову,за якою визначаємо чи існують в даному списку
#дієслова
and w[1][1].startswith('V') and w[1][0] in verbs]
a
#ввиводимо результат на екран
text=nltk.corpus.brown.tagged_words(categories='romance')
#Присвоюємо змінній text усі слова,які належать до корпусу brown
#категорії romance
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
#мінній а присвоюємо умову,за якою визначаємо чи існують в даному
#списку дієслова
text=nltk.corpus.brown.tagged_words(categories='religion')
#Присвоюємо змінній text усі слова,які  належать до корпусу brown
#категорії religion
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0] in verbs]
#змінній а присвоюємо умову,за якою визначаємо чи існують в даному
#списку дієслова
text=nltk.corpus.brown.tagged_words(categories='news')
#перевіряємо чи виконується наша умова,якщо брати інші частини
#мови в категорії news
a=[w for w in nltk.bigrams(text) if w[0][1].startswith('QL')
and w[1][1].startswith('V') and w[1][0]=='operated']
#умова,яку  ми присвоїли змінній а виконується,але в даній категорії відсутні
#слова,які дані нам в умові задачі,а саме adore,love,like,prefer

