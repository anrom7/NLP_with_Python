# Hanchevska Iryna, Chapter 5, Exercise 1

import nltk
from nltk.corpus import brown
def tag_text(text):
    tokens=nltk.word_tokenize(text)
    tagged_words=nltk.pos_tag(tokens) #tags each word
    return tagged_words

if __name__=='__main__':
    phrases=["British Left Waffles on Falkland Islands.","Juvenile Court to Try Shooting Defendant."]
    for ph in phrases:
        print "Phrase: %s" % (ph)
        print "Tagged words: %s" % (tag_text(ph)) #results
