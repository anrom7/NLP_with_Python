
import nltk
from nltk.corpus import brown
sents=brown.tagged_sents(categories='news') # ������ ����� � ���� � ����� �� 1 ���
def form_dict(sents):                       # �� ����� �������� ������ ���,
        cfd = nltk.ConditionalFreqDist()    # �� ����� �������� ������� ����� ����
        for (wd, tg) in sents:
            cfd[wd].inc(tg)
        amb_dict = nltk.defaultdict()
        for w in cfd.conditions():
            if len(cfd[w])>1:
                amb_dict[w] = len(cfd[w])
        sortedDict = sorted(amb_dict.items(), reverse=True)
        return sortedDict

print form_dict(nltk.corpus.brown.tagged_words(categories = 'news'))[:10]
