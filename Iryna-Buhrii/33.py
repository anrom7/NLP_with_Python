# Write a code that builds a dictionary of dictionaries of sets.
# Use it to store thset of POS tags that can follow a given POS tag.

import nltk
brown_tagged=nltk.corpus.brown.tagged_words()
def tag(word,tag):
    dictionary=dict()
    default_dictionary=nltk.defaultdict(dict)
# Building default dictionary.
    empty=[]
    for i in range(len(brown_tagged)-1):
        word_tag1=brown_tagged[i]
        word_tag2=brown_tagged[i+1]
        if word_tag1[0]==word and word_tag1[1]==tag:
            empty+=[word_tag2[1]]
    dictionary[tag]=set(empty)
    default_dictionary[word]=dictionary
# Building dictionary of dictionaries function.
    return default_dictionary
tag('green','JJ')
print 'Tags:'
print tag('green','JJ')
# Result.
