# Pushchinska_Iryna PRLs-11
# Chapter_5, Task_27

import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
train_sents = brown_tagged_sents[:1000]
test_sents = brown_tagged_sents[1000:1200]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
test_tags = [tag for sent in brown.sents(categories='news')
       for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
cm = nltk.ConfusionMatrix(gold_tags, test_tags)

mistakes=nltk.defaultdict(int)

for i in range(int(len(test_tags))):
	if test_tags[i] !=gold_tags [i]:
		pair=(test_tags [i], gold_tags [i])
		if pair not in mistakes:
			mistakes[pair]+=1

print cm.key(), '\n''List of mistakes',mistakes, '\n', 'Evaluation of the tagger t2:', t2.evaluate(test_sents)
