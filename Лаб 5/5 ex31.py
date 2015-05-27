
import nltk
from nltk.corpus import brown
def function(cfd, wordlist):
    t = dict((w, cfd[w].max()) for w in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=t, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='mystery'))
def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='mystery')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='mystery'))
    sizes = 2 ** pylab.arange(15)
    perfs = [function(cfd, words_by_freq[:size]) for size in sizes]
    pylab.semilogx(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Play with Varying Size')
    pylab.xlabel('Size')
    pylab.ylabel('Play')
    pylab.show()
    
display()

#� ���� ������� � ������ pylab.plot() �� pylab.semilogx().
#���������� ���������, �� ������ ��������� - ��� ��� ������, �������� ��� ������.
# ����� ������� ����������� �� 1
