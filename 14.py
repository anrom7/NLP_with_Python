# by Nataliia Masiuk
import nltk
from nltk.corpus import brown
tagged=brown.tagged_sents(categories='learned', simplify_tags=True)
train_data=tagged
for w in range (1,6):
    ngram=nltk.NgramTagger (w, tagged)
    print 'ngram, n=', w, ngram.evaluate(nltk.corpu.brown.tagged ())
# Word segmantation or sparse data problem is important in many tasks.
# As n gets larger here appears sparse data problem.
# Large data for training is needed for sparse data problem to reach more
#accurate results
