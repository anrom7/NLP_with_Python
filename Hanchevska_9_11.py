# Hanchevska Iryna, Chapter 9, Exercise 11
import nltk
from nltk import load_parser
tokens = 'Heute sieht der Hund die Katze'.split() #Sentence, where the verb is on
                                                  #the second place before subject
cp = load_parser('grammars/book_grammars/german_modified.fcfg') #Modified grammar, to which
                                                        #I added 2 lines # Adverbs
                                                                         #ADV -> 'Heute'
#With the modified german grammar parse our sentence
for tree in cp.nbest_parse(tokens):
    print tree

tree.draw()
