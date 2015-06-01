
import nltk
from nltk.corpus import brown
sents=brown.tagged_sents(categories='news') # Шукаємо слова у яких є більше ніж 1 тег
def form_dict(sents):                       # На виході отримуємо список слів,
        cfd = nltk.ConditionalFreqDist()    # які мають найбільшу кількість різних тегів
        for (wd, tg) in sents:
            cfd[wd].inc(tg)
        amb_dict = nltk.defaultdict()
        for w in cfd.conditions():
            if len(cfd[w])>1:
                amb_dict[w] = len(cfd[w])
        sortedDict = sorted(amb_dict.items(), reverse=True)
        return sortedDict

print form_dict(nltk.corpus.brown.tagged_words(categories = 'news'))[:10]
