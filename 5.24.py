import nltk
from nltk.corpus import brown
tagged_sents=brown.tagged_sents()
train_sents=tagged_sents[:1000] # dani dlia trenuvannja
diap=[1,2,3,4,5,6] # diapazon zna4enj
for i in diap:
	t=nltk.NgramTagger(n=i, train=train_sents)
	print 'N=',i, 'Evaluation:', t.evaluate (tagged_sents[1000:1200])
