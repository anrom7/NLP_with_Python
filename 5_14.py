#Author: Uliana Hentosh
import nltk
paru=nltk.corpus.brown.tagged_words()
tags=[tag for (word, tag) in paru] # extract all tags from pairs 'word,tag'
w=set(tags) # sorting with repetition of tags
print (sorted(w) [:20]) # sorting sorted w and eliminating duplicates
