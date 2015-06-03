# Hanchevska Iryna, Chapter 5, Exercise 28
import nltk
from nltk.tag.simplify import simplify_wsj_tag
from nltk.corpus import brown
tagged_sent = nltk.pos_tag(nltk.word_tokenize("And now for something completely different"))
tagged_sent
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
brown_news_tagged
 #NOUNS TAGS EXAMPLE:
word_tag_pairs = nltk.bigrams(brown_news_tagged)
word_tag_pairs
 #VERBS TAGS EXAMPLE:
my_var = nltk.corpus.treebank.tagged_words(simplify_tags=True)
my_var
word_tag_fd = nltk.FreqDist( my_var)
print word_tag_fd
