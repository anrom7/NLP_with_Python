Marta Zaremba PRLs 11
import nltk
nltk.data.show_cfg('grammars/book_grammars/german.fcfg') #German Grammar 
tokens1 = 'die Katze hilft dem Hund '.split() #Sentence 1
print tokens1
from nltk import load_parser
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree1 in cp.nbest_parse(tokens1):
    print tree1

tree1.draw()    
tokens2 = 'ich folge den Katzen'.split() #Sentence 2
print tokens2
for tree2 in cp.nbest_parse(tokens2):
    print tree2

tree2.draw()
#Transitive verbs have an object in accusative (tokens2) or dative case (tokens1).
#Intransitive verbs don't require any object.

