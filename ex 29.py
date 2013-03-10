import nltk
from nltk.corpus import brown

#Example
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
word_tag_pairs = nltk.bigrams(brown_news_tagged)
print list(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'N'))

#
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents) * 0.9) 

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]


bigram_tagger = nltk.BigramTagger(train_sents)
print bigram_tagger.tag(brown_sents[2007])

unseen_sent = brown_sents[4203]
print bigram_tagger.tag(unseen_sent)

print bigram_tagger.evaluate(test_sents)
