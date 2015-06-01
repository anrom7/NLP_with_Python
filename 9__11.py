#Anna Karbivska, Als-11
#9.6.11
#Extend the German grammar in Example 9-4 so that it can handle so-called verbsecond
#structures like the following:
#(63) Heute sieht der Hund die Katze.
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
